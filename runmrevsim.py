# Import the backtrader platform
import backtrader as bt

# For certain optimization parameter range inputs
import numpy as np

import time

from utilities import *

from meanreversion import MeanReversionStrategy

from wordyanalyzer import TradeAnalyzer

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
	with open("mrevResults.txt", "r") as f:
		with open("backupMrevResults.txt", "w") as bf:
			bf.write(f.read())

	open('mrevResults.txt', 'w').close()

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

	cerebroNFLX.addstrategy(MeanReversionStrategy, displayingStrategyLogs=True)
	cerebroNVDA.addstrategy(MeanReversionStrategy, displayingStrategyLogs=True)
	cerebroROKU.addstrategy(MeanReversionStrategy, displayingStrategyLogs=True)
	cerebroSQ.addstrategy(MeanReversionStrategy, displayingStrategyLogs=True)
	cerebroTSLA.addstrategy(MeanReversionStrategy, displayingStrategyLogs=True)
	
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

	with open("mrevResults.txt", "a") as f:
		for pAndSList in parametersAndStatistics:
			parameters = pAndSList[0]
			statistics = pAndSList[1]
			f.write("\n")
			f.write('firstTimeOfEntry: %s lastTimeOfEntry: %s maPeriod: %d goodCandlesBeforeEntry: %d atrRiskDenominator: %d minRRratio: %d consecutiveGoodCandles: %d' %
					(
						parameters[0],
						parameters[1],
						parameters[2],
						parameters[3],
						parameters[4],
						parameters[5],
						parameters[6]
					))
			f.write("\n")
			f.write('Trades: %d winrate: %s averageSize: %.4f centsPerWin: %.4f centsPerLoss: %.4f profitLossRatio: %.4f expectancy: %.4f PnL: %.4f' %
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