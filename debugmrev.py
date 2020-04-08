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
	comminfo = FixedCommissionScheme()

	dataSQ = MyDataFeed(dataname='data/MY_intraday_1min_SQ.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)

	parametersAndStatistics = []

	cerebroSQ = bt.Cerebro()

	cerebroSQ.addanalyzer(TradeAnalyzer, _name='ta')

	cerebroSQ.broker.setcash(100000.0)

	cerebroSQ.broker.addcommissioninfo(comminfo)

	cerebroSQ.adddata(dataSQ)

	cerebroSQ.addstrategy(MeanReversionStrategy, debugging=True, displayingStrategyLogs=True)
	
	sqStrat = cerebroSQ.run()[0]

	analyzerList = [sqStrat.analyzers.ta]

	parametersAndStatistics.append(getParametersAndStatistics(sqStrat, analyzerList))

	for pAndSList in parametersAndStatistics:
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