# Import the backtrader platform
import backtrader as bt

# For certain optimization parameter range inputs
import numpy as np

import time

from utilities import *

from meanreversion import MeanReversionStrategy

from silentanalyzer import TradeAnalyzer

import datetime  # For datetime objects

class MyDataFeed(bt.feeds.GenericCSVData):

  params = (
	('fromdate', datetime.datetime(2019, 1, 1)),
	('todate', datetime.datetime(2019, 12, 31)),
	('dtformat', ('=\"%Y-%m-%d\"')),
	('tmformat', ('%H.%M.%S')),

	('datetime', 0),
	('time', 1),
	('open', 2),
	('high', 3),
	('low', 4),
	('close', 5),
	('volume', 6),
	('openinterest', -1)
)

class FixedCommissionScheme(bt.CommInfoBase):
	'''
	This is a simple fixed commission scheme
	'''
	params = (
		('commission', 0.0),
		('stocklike', True),
		('commtype', bt.CommInfoBase.COMM_FIXED),
	)

	def _getcommission(self, size, price, pseudoexec):
		return self.params.commission + abs(size)/2000

def getParametersAndStatistics(strategy, analyzers):
	parametersAndStatistics = []
	parametersAndStatistics.append((
					strategy.params.firstTimeOfEntry,
					strategy.params.lastTimeOfEntry,
					strategy.params.maPeriod,
					strategy.params.goodCandlesBeforeEntry,
					strategy.params.atrRiskDenominator,
					strategy.params.minRRratio,
					strategy.params.consecutiveGoodCandles))

	tradeCount = 0
	wins = 0
	losses = 0
	totalShareSize = 0
	totalProfits = 0
	totalLosses = 0
	totalPnL = 0
	winrate = 0
	averageShareSize = 0.0
	centsPerWin = 0
	centsPerLoss = 0
	profitLossRatio = 0
	expectancy = 0
	for a in analyzers:
		tradeCount += a.tradeCount
		wins += a.wins
		losses += a.losses
		totalShareSize += a.totalSharesTraded
		totalProfits += a.totalProfits
		totalLosses += a.totalLosses
		totalPnL += a.pnl
	if tradeCount > 0:
		winrate = str(roundTo4Decimals(wins/tradeCount*100)) + '%'
		averageShareSize = totalShareSize/tradeCount
		if wins > 0:
			centsPerWin = totalProfits/averageShareSize/wins
		if losses > 0:
			centsPerLoss = totalLosses/averageShareSize/losses
		if centsPerLoss > 0:
			profitLossRatio = centsPerWin/centsPerLoss
		elif centsPerWin > 0:
			profitLossRatio = float("inf")
		expectancy = totalPnL/averageShareSize/tradeCount
	else:
		winrate = '0.0000%'

	parametersAndStatistics.append((tradeCount, winrate, averageShareSize, centsPerWin, centsPerLoss, profitLossRatio, expectancy, totalPnL))

	return parametersAndStatistics

if __name__ == '__main__':
	comminfo = FixedCommissionScheme()

	dataNFLX = MyDataFeed(dataname='data/MY_intraday_1min_NFLX.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataNVDA = MyDataFeed(dataname='data/MY_intraday_1min_NVDA.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataROKU = MyDataFeed(dataname='data/MY_intraday_1min_ROKU.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataSQ = MyDataFeed(dataname='data/MY_intraday_1min_SQ.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataTSLA = MyDataFeed(dataname='data/MY_intraday_1min_TSLA.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)

	parametersAndStatistics = []

	firstTimeOfEntryList = ['08:30:00', '08:35:00', '08:40:00', '08:45:00', '08:50:00']
	lastTimeOfEntryList = ['09:29:00']
	maPeriodList = [20]
	goodCandlesBeforeEntryList = [2, 3]
	atrRiskDenominatorList = [10]
	minRRratioList = [2, 3, 4]
	consecutiveGoodCandlesList = [2, 3, 4, 5, 6]

	start = time.time()

	for firstTimeOfEntryConfig in firstTimeOfEntryList:
		end = time.time()
		print('Currently running start time of: ' + firstTimeOfEntryConfig)
		print('Time elapsed: ' + str(end - start) + ' seconds (' + str((end - start)/60) + ' minutes)')
		for lastTimeOfEntryConfig in lastTimeOfEntryList:
			for maPeriodConfig in maPeriodList:
				for goodCandlesBeforeEntryConfig in goodCandlesBeforeEntryList:
					for atrRiskDenominatorConfig in atrRiskDenominatorList:
						for minRRratioConfig in minRRratioList:
							for consecutiveGoodCandlesConfig in consecutiveGoodCandlesList:

								cerebroNFLX = bt.Cerebro()
								cerebroNVDA = bt.Cerebro()
								cerebroROKU = bt.Cerebro()
								cerebroSQ = bt.Cerebro()
								cerebroTSLA = bt.Cerebro()

								cerebroNFLX.addanalyzer(TradeAnalyzer, _name='ta')
								cerebroNVDA.addanalyzer(TradeAnalyzer, _name='ta')
								cerebroROKU.addanalyzer(TradeAnalyzer, _name='ta')
								cerebroSQ.addanalyzer(TradeAnalyzer, _name='ta')
								cerebroTSLA.addanalyzer(TradeAnalyzer, _name='ta')

								cerebroNFLX.broker.setcash(100000.0)
								cerebroNVDA.broker.setcash(100000.0)
								cerebroROKU.broker.setcash(100000.0)
								cerebroSQ.broker.setcash(100000.0)
								cerebroTSLA.broker.setcash(100000.0)

								cerebroNFLX.broker.addcommissioninfo(comminfo)
								cerebroNVDA.broker.addcommissioninfo(comminfo)
								cerebroROKU.broker.addcommissioninfo(comminfo)
								cerebroSQ.broker.addcommissioninfo(comminfo)
								cerebroTSLA.broker.addcommissioninfo(comminfo)

								cerebroNFLX.adddata(dataNFLX)
								cerebroNVDA.adddata(dataNVDA)
								cerebroROKU.adddata(dataROKU)
								cerebroSQ.adddata(dataSQ)
								cerebroTSLA.adddata(dataTSLA)

								cerebroNFLX.addstrategy(MeanReversionStrategy, firstTimeOfEntry=firstTimeOfEntryConfig, lastTimeOfEntry=lastTimeOfEntryConfig, maPeriod=maPeriodConfig, goodCandlesBeforeEntry=goodCandlesBeforeEntryConfig, atrRiskDenominator=atrRiskDenominatorConfig, minRRratio=minRRratioConfig, consecutiveGoodCandles=consecutiveGoodCandlesConfig)
								cerebroNVDA.addstrategy(MeanReversionStrategy, firstTimeOfEntry=firstTimeOfEntryConfig, lastTimeOfEntry=lastTimeOfEntryConfig, maPeriod=maPeriodConfig, goodCandlesBeforeEntry=goodCandlesBeforeEntryConfig, atrRiskDenominator=atrRiskDenominatorConfig, minRRratio=minRRratioConfig, consecutiveGoodCandles=consecutiveGoodCandlesConfig)
								cerebroROKU.addstrategy(MeanReversionStrategy, firstTimeOfEntry=firstTimeOfEntryConfig, lastTimeOfEntry=lastTimeOfEntryConfig, maPeriod=maPeriodConfig, goodCandlesBeforeEntry=goodCandlesBeforeEntryConfig, atrRiskDenominator=atrRiskDenominatorConfig, minRRratio=minRRratioConfig, consecutiveGoodCandles=consecutiveGoodCandlesConfig)
								cerebroSQ.addstrategy(MeanReversionStrategy, firstTimeOfEntry=firstTimeOfEntryConfig, lastTimeOfEntry=lastTimeOfEntryConfig, maPeriod=maPeriodConfig, goodCandlesBeforeEntry=goodCandlesBeforeEntryConfig, atrRiskDenominator=atrRiskDenominatorConfig, minRRratio=minRRratioConfig, consecutiveGoodCandles=consecutiveGoodCandlesConfig)
								cerebroTSLA.addstrategy(MeanReversionStrategy, firstTimeOfEntry=firstTimeOfEntryConfig, lastTimeOfEntry=lastTimeOfEntryConfig, maPeriod=maPeriodConfig, goodCandlesBeforeEntry=goodCandlesBeforeEntryConfig, atrRiskDenominator=atrRiskDenominatorConfig, minRRratio=minRRratioConfig, consecutiveGoodCandles=consecutiveGoodCandlesConfig)

								nflxStrat = cerebroNFLX.run()[0]
								nvdaStrat = cerebroNVDA.run()[0]
								rokuStrat = cerebroROKU.run()[0]
								sqStrat = cerebroSQ.run()[0]
								tslaStrat = cerebroTSLA.run()[0]

								analyzerList = [
												nflxStrat.analyzers.ta,
												nvdaStrat.analyzers.ta,
												rokuStrat.analyzers.ta,
												sqStrat.analyzers.ta,
												tslaStrat.analyzers.ta
								]

								parametersAndStatistics.append(getParametersAndStatistics(tslaStrat, analyzerList))

	end = time.time()

	parametersAndStatistics = list(filter(lambda x: x[1][0] > 0, parametersAndStatistics))

	parametersAndStatistics.sort(key=lambda x: -x[1][7])

	reducedList = parametersAndStatistics[:12]

	for pAndSList in reducedList:
		parameters = pAndSList[0]
		statistics = pAndSList[1]
		print('firstTimeOfEntry: %s lastTimeOfEntry: %s maPeriod: %d goodCandlesBeforeEntry: %d atrRiskDenominator: %d minRRratio: %d consecutiveGoodCandles: %d' %
				(
					parameters[0],
					parameters[1],
					parameters[2],
					parameters[3],
					parameters[4],
					parameters[5],
					parameters[6]
				))
		print('Trades: %d winrate: %s averageSize: %.4f centsPerWin: %.4f centsPerLoss: %.4f profitLossRatio: %.4f expectancy: %.4f PnL: %.4f' %
				(
					statistics[0],
					statistics[1],
					statistics[2],
					statistics[3],
					statistics[4],
					statistics[5],
					statistics[6],
					statistics[7]
				))

	print ("")

	parametersAndStatistics.sort(key=lambda x: -x[1][6])

	reducedList = parametersAndStatistics[:12]

	for pAndSList in reducedList:
		parameters = pAndSList[0]
		statistics = pAndSList[1]
		print('firstTimeOfEntry: %s lastTimeOfEntry: %s maPeriod: %d goodCandlesBeforeEntry: %d atrRiskDenominator: %d minRRratio: %d consecutiveGoodCandles: %d' %
				(
					parameters[0],
					parameters[1],
					parameters[2],
					parameters[3],
					parameters[4],
					parameters[5],
					parameters[6]
				))
		print('Trades: %d winrate: %s averageSize: %.4f centsPerWin: %.4f centsPerLoss: %.4f profitLossRatio: %.4f PnL: %.4f expectancy: %.4f' %
				(
					statistics[0],
					statistics[1],
					statistics[2],
					statistics[3],
					statistics[4],
					statistics[5],
					statistics[7],
					statistics[6]
				))

	print('Time elapsed: ' + str(end - start) + ' seconds (' + str((end - start)/60) + ' minutes)')