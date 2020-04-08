# Import the backtrader platform
import backtrader as bt

# For certain optimization parameter range inputs
import numpy as np

import time

from utilities import *

from trendfollowing import TrendFollowingStrategy

from wordyanalyzer import TradeAnalyzer

import datetime  # For datetime objects

class MyDataFeed(bt.feeds.GenericCSVData):

  params = (
	('fromdate', datetime.datetime(2019, 1, 1)),
	('todate', datetime.datetime(2020, 12, 31)),
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
					strategy.params.entrySensitivityWindow,
					strategy.params.atrRiskDenominator,
					strategy.params.consecutiveGoodCandles,
					strategy.params.thresholdDenominator,
					strategy.params.lettingStopsHit,
					strategy.params.reversing))

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
	with open("trendResults.txt", "r") as f:
		with open("backupTrendResults.txt", "w") as bf:
			bf.write(f.read())

	open('trendResults.txt', 'w').close()

	comminfo = FixedCommissionScheme()

	dataAMD = MyDataFeed(dataname='data/MY_intraday_1min_AMD.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataMU = MyDataFeed(dataname='data/MY_intraday_1min_MU.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataNFLX = MyDataFeed(dataname='data/MY_intraday_1min_NFLX.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataNVDA = MyDataFeed(dataname='data/MY_intraday_1min_NVDA.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataROKU = MyDataFeed(dataname='data/MY_intraday_1min_ROKU.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataSQ = MyDataFeed(dataname='data/MY_intraday_1min_SQ.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	# dataTSLA = MyDataFeed(dataname='data/MY_intraday_1min_TSLA.csv',
	# 					timeframe=bt.TimeFrame.Minutes, compression=1)

	parametersAndStatistics = []

	cerebroAMD = bt.Cerebro()
	cerebroMU = bt.Cerebro()
	cerebroNFLX = bt.Cerebro()
	cerebroNVDA = bt.Cerebro()
	cerebroROKU = bt.Cerebro()
	cerebroSQ = bt.Cerebro()
	# cerebroTSLA = bt.Cerebro()

	cerebroAMD.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroMU.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroNFLX.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroNVDA.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroROKU.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroSQ.addanalyzer(TradeAnalyzer, _name='ta')
	# cerebroTSLA.addanalyzer(TradeAnalyzer, _name='ta')

	cerebroAMD.broker.setcash(100000.0)
	cerebroMU.broker.setcash(100000.0)
	cerebroNFLX.broker.setcash(100000.0)
	cerebroNVDA.broker.setcash(100000.0)
	cerebroROKU.broker.setcash(100000.0)
	cerebroSQ.broker.setcash(100000.0)
	# cerebroTSLA.broker.setcash(100000.0)

	cerebroAMD.broker.addcommissioninfo(comminfo)
	cerebroMU.broker.addcommissioninfo(comminfo)
	cerebroNFLX.broker.addcommissioninfo(comminfo)
	cerebroNVDA.broker.addcommissioninfo(comminfo)
	cerebroROKU.broker.addcommissioninfo(comminfo)
	cerebroSQ.broker.addcommissioninfo(comminfo)
	# cerebroTSLA.broker.addcommissioninfo(comminfo)

	cerebroAMD.adddata(dataAMD)
	cerebroMU.adddata(dataMU)
	cerebroNFLX.adddata(dataNFLX)
	cerebroNVDA.adddata(dataNVDA)
	cerebroROKU.adddata(dataROKU)
	cerebroSQ.adddata(dataSQ)
	# cerebroTSLA.adddata(dataTSLA)

	cerebroAMD.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroMU.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroNFLX.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroNVDA.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroROKU.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroSQ.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	# cerebroTSLA.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	
	amdStrat = cerebroAMD.run()[0]
	muStrat = cerebroMU.run()[0]
	nflxStrat = cerebroNFLX.run()[0]
	nvdaStrat = cerebroNVDA.run()[0]
	rokuStrat = cerebroROKU.run()[0]
	sqStrat = cerebroSQ.run()[0]
	# tslaStrat = cerebroTSLA.run()[0]

	analyzerList = [
					amdStrat.analyzers.ta,
					muStrat.analyzers.ta,
					nflxStrat.analyzers.ta,
					nvdaStrat.analyzers.ta,
					rokuStrat.analyzers.ta,
					sqStrat.analyzers.ta
					# tslaStrat.analyzers.ta
	]

	parametersAndStatistics.append(getParametersAndStatistics(rokuStrat, analyzerList))

	with open("trendResults.txt", "a") as f:
		for pAndSList in parametersAndStatistics:
			parameters = pAndSList[0]
			statistics = pAndSList[1]
			f.write("\n")
			f.write('firstTimeOfEntry: %s lastTimeOfEntry: %s maPeriod: %d entrySensitivityWindow: %d atrRiskDenominator: %.2f consecutiveGoodCandles: %d thresholdDenominator: %d lettingStopsHit: %s reversing: %s' %
					(
						parameters[0],
						parameters[1],
						parameters[2],
						parameters[3],
						parameters[4],
						parameters[5],
						parameters[6],
						parameters[7],
						parameters[8]
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
			print('firstTimeOfEntry: %s lastTimeOfEntry: %s maPeriod: %d entrySensitivityWindow: %d atrRiskDenominator: %.2f consecutiveGoodCandles: %d thresholdDenominator: %d lettingStopsHit: %s reversing: %s' %
					(
						parameters[0],
						parameters[1],
						parameters[2],
						parameters[3],
						parameters[4],
						parameters[5],
						parameters[6],
						parameters[7],
						parameters[8]
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