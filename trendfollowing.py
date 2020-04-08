import backtrader as bt

from utilities import *

# Create a Strategy
class TrendFollowingStrategy(bt.Strategy):

	params = (
		('firstTimeOfEntry', '08:50:00'),
		('lastTimeOfEntry', '09:29:00'),
		('maPeriod', 20),
		('entrySensitivityWindow', 1),
		('atrRiskDenominator', 10),
		('consecutiveGoodCandles', 3),
		('thresholdDenominator', 2),
		('lettingStopsHit', True),
		('reversing', False),
		('debugging', False),
		('displayingStrategyLogs', False)
	)

	'''

-------------------- Latest Sim Result --------------------

firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 163 winrate: 43.5583% averageSize: 211.9325 centsPerWin: 59.3481 centsPerLoss: 24.9484 profitLossRatio: 2.3788 expectancy: 0.1177 PnL: 4065.8320

firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 154 winrate: 46.1039% averageSize: 219.6818 centsPerWin: 57.2258 centsPerLoss: 23.2606 profitLossRatio: 2.4602 expectancy: 0.1385 PnL: 4684.4932

firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 148 winrate: 45.9459% averageSize: 225.2770 centsPerWin: 55.8707 centsPerLoss: 22.4819 profitLossRatio: 2.4851 expectancy: 0.1352 PnL: 4507.0142

firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 137 winrate: 41.6058% averageSize: 234.7518 centsPerWin: 55.0927 centsPerLoss: 21.5075 profitLossRatio: 2.5616 expectancy: 0.1036 PnL: 3332.7319

firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 131 winrate: 44.2748% averageSize: 241.2214 centsPerWin: 54.2124 centsPerLoss: 20.7968 profitLossRatio: 2.6068 expectancy: 0.1241 PnL: 3922.6241

firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 126 winrate: 45.2381% averageSize: 247.7222 centsPerWin: 53.7225 centsPerLoss: 20.2791 profitLossRatio: 2.6492 expectancy: 0.1320 PnL: 4119.4391

-------------------- Backtest Results --------------------

Normal (PnL Focus):
firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 163 winrate: 43.5583% averageSize: 211.9325 centsPerWin: 59.3481 centsPerLoss: 24.9484 profitLossRatio: 2.3788 expectancy: 0.1177 PnL: 4065.8320

Normal (PnL & Efficiency):
firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 163 winrate: 43.5583% averageSize: 211.9325 centsPerWin: 59.3481 centsPerLoss: 24.9484 profitLossRatio: 2.3788 expectancy: 0.1177 PnL: 4065.8320

Normal (Efficiency Focus):
firstTimeOfEntry: 08:35:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 40 winrate: 42.5% averageSize: 203.8500 centsPerWin: 104.1943 centsPerLoss: 30.8196 profitLossRatio: 3.3808 PnL: 2165.8081 expectancy: 0.2656

Normal (Efficiency & PnL):
firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 47 winrate: 42.5532% averageSize: 220.4681 centsPerWin: 100.6236 centsPerLoss: 29.4560 profitLossRatio: 3.4161 PnL: 2683.4480 expectancy: 0.2590

Normal (Win Rate Focus):
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 393 averageSize: 127.4784 centsPerWin: 34.6286 centsPerLoss: 28.6266 profitLossRatio: 1.2097 expectancy: 0.0533 PnL: 2672.7002 winrate: 53.6896%

firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 658 winrate: 51.5198% averageSize: 187.0775 centsPerWin: 23.1664 centsPerLoss: 18.5349 profitLossRatio: 1.2499 expectancy: 0.0295 PnL: 3630.7625
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 649 winrate: 52.0801% averageSize: 188.3744 centsPerWin: 22.8161 centsPerLoss: 18.6043 profitLossRatio: 1.2264 expectancy: 0.0297 PnL: 3627.9222
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 209 winrate: 44.0191% averageSize: 308.5789 centsPerWin: 28.2300 centsPerLoss: 15.7500 profitLossRatio: 1.7924 expectancy: 0.0361 PnL: 2327.9453
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 211 winrate: 43.128% averageSize: 307.1185 centsPerWin: 28.6083 centsPerLoss: 15.7308 profitLossRatio: 1.8186 expectancy: 0.0339 PnL: 2197.9295
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 126 winrate: 50.7937% averageSize: 198.1984 centsPerWin: 36.8541 centsPerLoss: 24.7026 profitLossRatio: 1.4919 expectancy: 0.0656 PnL: 1639.3018
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 130 winrate: 49.2308% averageSize: 194.2231 centsPerWin: 37.7171 centsPerLoss: 24.4802 profitLossRatio: 1.5407 expectancy: 0.0614 PnL: 1550.2942
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 28 winrate: 32.1429% averageSize: 302.2500 centsPerWin: 55.8783 centsPerLoss: 18.1564 profitLossRatio: 3.0776 expectancy: 0.0564 PnL: 477.3523
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 29 winrate: 31.0345% averageSize: 296.4138 centsPerWin: 56.9785 centsPerLoss: 18.6426 profitLossRatio: 3.0564 expectancy: 0.0483 PnL: 414.8423

firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 126 winrate: 50.7937% averageSize: 198.1984 centsPerWin: 36.8541 centsPerLoss: 24.7026 profitLossRatio: 1.4919 PnL: 1639.3018 expectancy: 0.0656
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 130 winrate: 49.2308% averageSize: 194.2231 centsPerWin: 37.7171 centsPerLoss: 24.4802 profitLossRatio: 1.5407 PnL: 1550.2942 expectancy: 0.0614
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 28 winrate: 32.1429% averageSize: 302.2500 centsPerWin: 55.8783 centsPerLoss: 18.1564 profitLossRatio: 3.0776 PnL: 477.3523 expectancy: 0.0564
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 29 winrate: 31.0345% averageSize: 296.4138 centsPerWin: 56.9785 centsPerLoss: 18.6426 profitLossRatio: 3.0564 PnL: 414.8423 expectancy: 0.0483
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 209 winrate: 44.0191% averageSize: 308.5789 centsPerWin: 28.2300 centsPerLoss: 15.7500 profitLossRatio: 1.7924 PnL: 2327.9453 expectancy: 0.0361
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 211 winrate: 43.128% averageSize: 307.1185 centsPerWin: 28.6083 centsPerLoss: 15.7308 profitLossRatio: 1.8186 PnL: 2197.9295 expectancy: 0.0339
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 649 winrate: 52.0801% averageSize: 188.3744 centsPerWin: 22.8161 centsPerLoss: 18.6043 profitLossRatio: 1.2264 PnL: 3627.9222 expectancy: 0.0297
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 658 winrate: 51.5198% averageSize: 187.0775 centsPerWin: 23.1664 centsPerLoss: 18.5349 profitLossRatio: 1.2499 PnL: 3630.7625 expectancy: 0.0295

firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 649 averageSize: 188.3744 centsPerWin: 22.8161 centsPerLoss: 18.6043 profitLossRatio: 1.2264 expectancy: 0.0297 PnL: 3627.9222 winrate: 52.0801%
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 658 averageSize: 187.0775 centsPerWin: 23.1664 centsPerLoss: 18.5349 profitLossRatio: 1.2499 expectancy: 0.0295 PnL: 3630.7625 winrate: 51.5198%
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 126 averageSize: 198.1984 centsPerWin: 36.8541 centsPerLoss: 24.7026 profitLossRatio: 1.4919 expectancy: 0.0656 PnL: 1639.3018 winrate: 50.7937%
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 10.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 130 averageSize: 194.2231 centsPerWin: 37.7171 centsPerLoss: 24.4802 profitLossRatio: 1.5407 expectancy: 0.0614 PnL: 1550.2942 winrate: 49.2308%
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 209 averageSize: 308.5789 centsPerWin: 28.2300 centsPerLoss: 15.7500 profitLossRatio: 1.7924 expectancy: 0.0361 PnL: 2327.9453 winrate: 44.0191%
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 13:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 211 averageSize: 307.1185 centsPerWin: 28.6083 centsPerLoss: 15.7308 profitLossRatio: 1.8186 expectancy: 0.0339 PnL: 2197.9295 winrate: 43.128%
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: False
Trades: 28 averageSize: 302.2500 centsPerWin: 55.8783 centsPerLoss: 18.1564 profitLossRatio: 3.0776 expectancy: 0.0564 PnL: 477.3523 winrate: 32.1429%
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 entrySensitivityWindow: 1 atrRiskDenominator: 20.00 consecutiveGoodCandles: 3 thresholdDenominator: 2 lettingStopsHit: True reversing: True
Trades: 29 averageSize: 296.4138 centsPerWin: 56.9785 centsPerLoss: 18.6426 profitLossRatio: 3.0564 expectancy: 0.0483 PnL: 414.8423 winrate: 31.0345%

	'''

	maxRiskPerTrade = 60.00

	atrPeriod = 5

	endOfSession = '14:58:00'

	backupFileName = 'backupTrendResults.txt'
	filename = 'trendResults.txt'

	def __init__(self):
		# Keep references to the "open", "high", "low", "close", and "volume" lines
		self.dataopen = self.data.open
		self.datahigh = self.data.high
		self.datalow = self.data.low
		self.dataclose = self.data.close
		self.datavol = self.data.volume

		# Keep track of system signals and potential entry and exit points
		self.potentialEntryLong = None
		self.potentialExitFromLong = None
		self.potentialEntryShort = None
		self.potentialExitFromShort = None
		self.sma = 0
		self.closes = {}
		self.closeKey = 0
		self.slopeReference = 0
		self.closeTotal = 0
		self.vwap = 0
		self.volumePriceProductSum = 0
		self.totalVolume = 0
		self.atr = 0
		self.atrSum = 0
		self.dailyCloses = []
		self.dayCounter = 0
		self.currentDayHigh = -float("inf")
		self.currentDayLow = float("inf")
		self.diffs = {}
		self.diffsKey = 0
		self.lastTime = None
		self.validTimeLen = 1
		self.consecutiveBarCounter = 0
		self.lastGoodPrice = None
		self.justEnteredOrderToClose = False
		self.justEnteredOrderToCloseForTheDay = False

		# Keep track of initial position size and stop distance for all trades
		self.initialSize = None
		self.dollarRisk = None

		# Keep track of orders
		self.currentMarketOrder = None
		self.currentStopOrder = None
		self.currentTargetOrder = None
		self.cancelledToReverse = False

		# Keep track of the current day for daily parameter resets
		self.currentDay = self.data.datetime.date(0).isoformat()

	def log(self, txt, date=None, time=None):
		''' Logging function for this strategy'''
		date = date or self.data.datetime.date(0)
		time = time or self.data.datetime.time(0)
		print('%s, %s, %s' % (date.isoformat(), time.isoformat(), txt))

		with open(self.filename, "a") as f:
			f.write('%s, %s, %s' % (date.isoformat(), time.isoformat(), txt))
			f.write("\n")

	def notify_order(self, order):
		if order.status in [order.Submitted, order.Accepted]:

			if self.params.debugging:
				if order.status == order.Accepted:
					self.log('Order Submitted. Ref: ' + str(order.ref))
				else:
					self.log('Order Accepted. Ref: ' + str(order.ref))
			
			return

		# Check if an order has been completed
		# Attention: broker could reject order if not enough cash
		if order.status in [order.Completed]:

			if self.params.debugging:
				self.log('Order completed. Ref: ' + str(order.ref))

			if order.isbuy():

				if self.params.displayingStrategyLogs:
					self.log('BUY EXECUTED, Size: %.2f, Price: %.2f, Comm %.2f' %
					(
						order.executed.size,
						order.executed.price,
						order.executed.comm)
					)

				if self.position:

					if not self.cancelledToReverse:

						self.currentStopOrder = self.sell(
									size=self.initialSize,
									price=roundedNumber(order.executed.price -
										self.dollarRisk),
									exectype=bt.Order.Stop,
									valid=bt.Order.DAY)

						if self.params.displayingStrategyLogs:
							self.log('Sell stop order created. Ref: '
								+ str(self.currentStopOrder.ref))

						self.lastGoodPrice = order.executed.price

					else:

						self.cancelledToReverse = False

			else:

				if self.params.displayingStrategyLogs:
					self.log('SELL EXECUTED, Size: %.2f, Price: %.2f, Comm %.2f' %
					(
						order.executed.size,
						order.executed.price,
						order.executed.comm)
					)

				if self.position:

					if not self.cancelledToReverse:

						self.currentStopOrder = self.buy(
									size=self.initialSize,
									price=roundedNumber(order.executed.price +
										self.dollarRisk),
									exectype=bt.Order.Stop,
									valid=bt.Order.DAY)

						if self.params.displayingStrategyLogs:
							self.log('Buy stop order created. Ref: '
								+ str(self.currentStopOrder.ref))

						self.lastGoodPrice = order.executed.price

					else:

						self.cancelledToReverse = False

		elif order.status in [order.Canceled, order.Margin, order.Rejected]:

			if self.params.displayingStrategyLogs:
				if order.status == order.Canceled:
					self.log('Order Canceled. Ref: ' + str(order.ref))
				if order.status == order.Margin:
					self.log('Order Margin.' + str(order.ref))
				if order.status == order.Rejected:
					self.log('Order Rejected.' + str(order.ref))

		if not self.position:

			self.consecutiveBarCounter = 0
			self.lastGoodPrice = None

	def notify_trade(self, trade):
		if not trade.isclosed:

			return

		if self.params.displayingStrategyLogs:
			self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
				(trade.pnl, trade.pnlcomm))

	def logCurrentBarStats(self):
		self.log('currentBarOpen: ' + str(roundedNumber(self.dataopen[0]))
				+ ' currentBarClose: ' + str(roundedNumber(self.dataclose[0])))
		self.log('currentBarHigh: ' + str(roundedNumber(self.datahigh[0]))
				+ ' currentBarLow: ' + str(roundedNumber(self.datalow[0])))
		self.log(str(self.params.maPeriod) + ' SMA: ' + str(self.sma))
		self.log('VWAP: ' + str(self.vwap))

	def logDailyStats(self):
		self.log('previousDayClose: ' + str(self.dailyCloses[-1]))
		self.log('currentDayHigh: ' + str(self.currentDayHigh)
				+ ' currentDayLow: ' + str(self.currentDayLow))
		self.log('ATR: ' + str(self.atr))
		self.log('Dollar Risk: ' + str(self.dollarRisk))

	def logDecisionMetrics(self, potentialEntry, potentialExit, candleStrength,
							positionIsLong):
		if positionIsLong:
			self.log('Potential Entry Long: ' + str(potentialEntry)
						+ ' Potential Stop: ' + str(potentialExit))
			self.log('BullishStrength: ' + str(candleStrength))
		else:
			self.log('Potential Entry Short: ' + str(potentialEntry)
						+ ' Potential Stop: ' + str(potentialExit))
			self.log('BearishStrength: ' + str(candleStrength))

	def logOrderDecision(self, orderDecision, Price):
		self.log(orderDecision)
		self.log('Price: %.2f' % Price)

	def getMaxValidTradeTime(self):

		if self.params.consecutiveGoodCandles == 1:

			return '14:57:00'

		if self.params.consecutiveGoodCandles == 2:

			return '14:56:00'

		if self.params.consecutiveGoodCandles == 3:

			return '14:55:00'

		if self.params.consecutiveGoodCandles == 4:

			return '14:54:00'

		if self.params.consecutiveGoodCandles == 5:

			return '14:53:00'

		if self.params.consecutiveGoodCandles == 6:

			return '14:52:00'

		if self.params.consecutiveGoodCandles == 7:

			return '14:51:00'

		if self.params.consecutiveGoodCandles == 8:

			return '14:50:00'

		if self.params.consecutiveGoodCandles == 9:

			return '14:49:00'

		if self.params.consecutiveGoodCandles == 10:

			return '14:48:00'

	def manageTrade(self):
		if self.data.datetime.time(0).isoformat() < self.endOfSession:

			if self.position.size > 0:

				if (roundedNumber(self.dataclose[0]) >=
					roundedNumber(self.dataopen[0])):

					if (not self.params.lettingStopsHit and
						roundedNumber(self.dataclose[0]) < self.sma and
						roundedNumber(self.dataclose[0]) <
							roundedNumber(self.currentStopOrder.price +
											self.dollarRisk)):

						if self.params.debugging:
							self.log('Price closed in strength below the SMA'
								+ ' and entry when long, exiting now')

						self.cancel(self.currentStopOrder)

						self.close()

						return True

					else:

						self.consecutiveBarCounter += 1

				else:

					self.consecutiveBarCounter = 0

					if (self.params.reversing and
						self.currentStopOrder.status == bt.Order.Accepted and
						self.data.datetime.time(0).isoformat() <
							self.params.lastTimeOfEntry and
						self.validTimeLen >= 2 and
						roundedNumber(self.dataclose[0]) < self.sma and
						self.sma < self.vwap and
						roundedNumber(self.dataclose[0]) <
							self.slopeReference and
						roundedNumber(self.dataclose[-1]) <
							roundedNumber(self.dataopen[-1]) and
						roundedNumber(getMaxAdverseExcursion(self.datahigh,
									self.params.entrySensitivityWindow, False) -
									self.dataclose[0]) < self.dollarRisk and
						roundedNumber(self.vwap - self.dataclose[0]) <
							self.dollarRisk
						):

						if self.params.debugging:
							self.log('Setup condition to go the other way'
								+ ' occurred, exiting now in order to reverse')
							self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

						self.cancel(self.currentStopOrder)

						self.close()

						self.cancelledToReverse = True

						return True

				if (self.consecutiveBarCounter ==
					self.params.consecutiveGoodCandles):

					if (
						roundedNumber(self.dataclose[0]) >
							roundedNumber(self.lastGoodPrice +
											self.dollarRisk/
											self.params.thresholdDenominator) or
						(self.data.datetime.time(0).isoformat() <
							self.params.lastTimeOfEntry and
						self.validTimeLen >= 2 and
						roundedNumber(self.dataclose[0]) >
							roundedNumber(self.dataopen[0]) and
						roundedNumber(self.dataclose[0]) > self.sma and
						self.sma > self.vwap and
						roundedNumber(self.dataclose[0]) >
							self.slopeReference and
						roundedNumber(self.dataclose[-1]) >
							roundedNumber(self.dataopen[-1]) and
						roundedNumber(self.dataclose[0] - getMaxAdverseExcursion(
										self.datalow,
										self.params.entrySensitivityWindow, True
										)) < self.dollarRisk and
						roundedNumber(self.dataclose[0] - self.vwap) <
							self.dollarRisk
						)):

						self.consecutiveBarCounter = 0
						self.lastGoodPrice = roundedNumber(self.dataclose[0])

					else:

						if self.params.debugging:
							self.log(str(self.params.consecutiveGoodCandles)
								+ ' consecutive good candles closed at a price'
								+ ' inferior enough to exit, exiting now')
							self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

						self.cancel(self.currentStopOrder)

						self.close()

						return True

				if (self.consecutiveBarCounter == 0 and
					self.data.datetime.time(0).isoformat() >
						self.getMaxValidTradeTime()):

					if self.params.debugging:
						self.log('It is impossible for '
							+ str(self.params.consecutiveGoodCandles)
								+ ' consecutive candles to close before the end'
								+ ' of the day, exiting now')
						self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

					self.cancel(self.currentStopOrder)

					self.close()

					self.justEnteredOrderToCloseForTheDay = True

					return True

			else:

				if (roundedNumber(self.dataclose[0]) <=
					roundedNumber(self.dataopen[0])):

					if (not self.params.lettingStopsHit and
						roundedNumber(self.dataclose[0]) > self.sma and
						roundedNumber(self.dataclose[0]) >
							roundedNumber(self.currentStopOrder.price -
											self.dollarRisk)):

						if self.params.debugging:
							self.log('Price closed in strength above the SMA'
								+ ' and entry when short, exiting now')

						self.cancel(self.currentStopOrder)

						self.close()

						return True

					else:

						self.consecutiveBarCounter += 1

				else:

					self.consecutiveBarCounter = 0

					if (self.params.reversing and
						self.currentStopOrder.status == bt.Order.Accepted and
						self.data.datetime.time(0).isoformat() <
							self.params.lastTimeOfEntry and
						self.validTimeLen >= 2 and
						roundedNumber(self.dataclose[0]) > self.sma and
						self.sma > self.vwap and
						roundedNumber(self.dataclose[0]) >
							self.slopeReference and
						roundedNumber(self.dataclose[-1]) >
							roundedNumber(self.dataopen[-1]) and
						roundedNumber(self.dataclose[0] - getMaxAdverseExcursion(
										self.datalow,
										self.params.entrySensitivityWindow, True
										)) < self.dollarRisk and
						roundedNumber(self.dataclose[0] - self.vwap) <
							self.dollarRisk
						):

						if self.params.debugging:
							self.log('Setup condition to go the other way'
								+ ' occurred, exiting now in order to reverse')
							self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

						self.cancel(self.currentStopOrder)

						self.close()

						self.cancelledToReverse = True

						return True

				if (self.consecutiveBarCounter ==
					self.params.consecutiveGoodCandles):

					if (
						roundedNumber(self.dataclose[0]) <
							roundedNumber(self.lastGoodPrice -
											self.dollarRisk/
											self.params.thresholdDenominator) or
						(self.data.datetime.time(0).isoformat() <
							self.params.lastTimeOfEntry and
						self.validTimeLen >= 2 and
						roundedNumber(self.dataclose[0]) <
							roundedNumber(self.dataopen[0]) and
						roundedNumber(self.dataclose[0]) < self.sma and
						self.sma < self.vwap and
						roundedNumber(self.dataclose[0] <
							self.slopeReference) and
						roundedNumber(self.dataclose[-1]) <
							roundedNumber(self.dataopen[-1]) and
						roundedNumber(getMaxAdverseExcursion(self.datahigh,
									self.params.entrySensitivityWindow, False) -
									self.dataclose[0]) < self.dollarRisk and
						roundedNumber(self.vwap - self.dataclose[0]) <
							self.dollarRisk
						)):

						self.consecutiveBarCounter = 0
						self.lastGoodPrice = roundedNumber(self.dataclose[0])

					else:

						if self.params.debugging:
							self.log(str(self.params.consecutiveGoodCandles)
								+ ' consecutive good candles closed equal to or'
								+ ' higher than the same price as my short'
								+ ' entry, or the last time this happened,'
								+ ' exiting now')
							self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

						self.cancel(self.currentStopOrder)

						self.close()

						return True

				if (self.consecutiveBarCounter == 0 and
					self.data.datetime.time(0).isoformat() >
						self.getMaxValidTradeTime()):

					if self.params.debugging:
						self.log('It is impossible for '
							+ str(self.params.consecutiveGoodCandles)
							+ ' consecutive candles to close before the end of'
							+ ' the day, exiting now')
						self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

					self.cancel(self.currentStopOrder)

					self.close()

					self.justEnteredOrderToCloseForTheDay = True

					return True

		elif not self.justEnteredOrderToCloseForTheDay:

			if self.params.debugging:
				self.log('Closing position and cancelling open orders'
					+ ' to avoid holding overnight')
				self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

			self.cancel(self.currentStopOrder)

			self.close()

			self.justEnteredOrderToCloseForTheDay = True

			return True

		return False

	def setDollarRiskAndInitialSize(self):
		self.dollarRisk = roundedNumber(self.atr/self.params.atrRiskDenominator)
		if self.dollarRisk > 0:
			self.initialSize = roundToInt(self.maxRiskPerTrade/self.dollarRisk)
		else:
			self.initialSize = 0

	def setUpOrderIfPossible(self):
		####### See if I have a setup to go Long #######

		self.potentialEntryLong = roundedNumber(self.dataclose[0])
		self.potentialExitFromLong = roundedNumber(
									self.potentialEntryLong - self.dollarRisk)
		bullishStrength = roundedNumber(self.dataclose[0] - self.dataopen[0])

		if (bullishStrength > 0 and
			roundedNumber(self.dataclose[0]) > self.sma and
			self.sma > self.vwap and
			roundedNumber(self.dataclose[0]) > self.slopeReference and
			roundedNumber(self.dataclose[-1]) >
				roundedNumber(self.dataopen[-1]) and
			roundedNumber(self.dataclose[0] - getMaxAdverseExcursion(
										self.datalow,
										self.params.entrySensitivityWindow, True
										)) < self.dollarRisk and
			roundedNumber(self.dataclose[0] - self.vwap) < self.dollarRisk
			):

			if self.params.displayingStrategyLogs:
				self.logDecisionMetrics(self.potentialEntryLong,
									self.potentialExitFromLong, bullishStrength,
									True)
				self.logOrderDecision('ENTERING MARKET ORDER LONG',
										self.potentialEntryLong)

			self.currentMarketOrder = self.buy(
											size=self.initialSize,
											exectype=bt.Order.Market,
											valid=bt.Order.DAY)

			return

		####### See if I have a setup to go Short #######

		self.potentialEntryShort = roundedNumber(self.dataclose[0])
		self.potentialExitFromShort = roundedNumber(
									self.potentialEntryShort + self.dollarRisk)

		if (bullishStrength < 0 and
			roundedNumber(self.dataclose[0]) < self.sma and
			self.sma < self.vwap and
			roundedNumber(self.dataclose[0]) < self.slopeReference and
			roundedNumber(self.dataclose[-1]) <
				roundedNumber(self.dataopen[-1]) and
			roundedNumber(getMaxAdverseExcursion(self.datahigh,
									self.params.entrySensitivityWindow, False) -
									self.dataclose[0]) < self.dollarRisk and
			roundedNumber(self.vwap - self.dataclose[0]) < self.dollarRisk
			):

			if self.params.displayingStrategyLogs:
				self.logDecisionMetrics(self.potentialEntryShort,
								self.potentialExitFromShort, -bullishStrength,
								False)
				self.logOrderDecision('ENTERING MARKET ORDER SHORT',
										self.potentialEntryShort)

			self.currentMarketOrder = self.sell(
											size=self.initialSize,
											exectype=bt.Order.Market,
											valid=bt.Order.DAY)

			return

	def calculateATR(self):
		self.diffsKey += 1
		if self.diffsKey > self.atrPeriod:
			self.diffsKey = 1
		if len(self.diffs) == self.atrPeriod:
			self.atrSum -= self.diffs[self.diffsKey]
		currentdiffs = []
		currentdiffs.append(roundedNumber(abs(self.currentDayHigh -
										self.dailyCloses[-1])))
		currentdiffs.append(roundedNumber(abs(self.currentDayLow -
										self.dailyCloses[-1])))
		currentdiffs.append(roundedNumber(self.currentDayHigh - self.currentDayLow))
		self.diffs[self.diffsKey] = max(currentdiffs)
		self.atrSum += max(currentdiffs)
		self.atr = roundedNumber(self.atrSum/len(self.diffs))

	def next(self):
		if self.data.datetime.date(0).isoformat() != self.currentDay:

			if self.params.debugging:
				self.log('Position Size: ' + str(self.position.size))

			if self.position.size > 0:

				self.log('ERROR: POSITION SIZE IS NOT EQUAL TO ZERO AT THE'
					+ ' START OF A NEW DAY. THERE IS A BUG SOMEWHERE.')

				raise bt.StrategySkipError

			# Set and reset daily trackers
			self.currentDay = self.data.datetime.date(0).isoformat()
			self.sma = 0
			self.closes = {}
			self.closeKey = 0
			self.slopeReference = roundedNumber(self.dataclose[0])
			self.closeTotal = 0
			self.vwap = 0
			self.volumePriceProductSum = 0
			self.totalVolume = 0

			if len(self.dailyCloses) > 0:

				self.calculateATR()
				self.setDollarRiskAndInitialSize()

			if self.dayCounter > 0:

				self.dailyCloses.append(roundedNumber(self.dataclose[-1]))

			self.dayCounter += 1
			self.currentDayHigh = -float("inf")
			self.currentDayLow = float("inf")
			self.validTimeLen = 1
			self.justEnteredOrderToCloseForTheDay = False

			if self.params.debugging and len(self.dailyCloses) > 0:
				self.logDailyStats()

		self.closeKey += 1

		if self.closeKey > self.params.maPeriod:

			self.closeKey = 1

		if len(self.closes) == self.params.maPeriod:

			self.slopeReference = self.closes[self.closeKey]
			self.closeTotal -= self.slopeReference

		self.closes[self.closeKey] = roundedNumber(self.dataclose[0])
		self.closeTotal += roundedNumber(self.dataclose[0])

		self.sma = roundedNumber(self.closeTotal/len(self.closes))

		self.volumePriceProductSum += roundedNumber((self.dataopen[0] +
													self.datahigh[0] +
													self.datalow[0] +
													self.dataclose[0])*
													self.datavol[0]/4)
		self.totalVolume += self.datavol[0]

		if self.totalVolume > 0:

			self.vwap = roundedNumber(
									self.volumePriceProductSum/self.totalVolume)

		if roundedNumber(self.datahigh[0]) > self.currentDayHigh:

			self.currentDayHigh = roundedNumber(self.datahigh[0])

		if roundedNumber(self.datalow[0]) < self.currentDayLow:

			self.currentDayLow = roundedNumber(self.datalow[0])

		if (self.lastTime != None and lastTimesValid(self.lastTime,
			self.data.datetime.time(0).isoformat(), 1)):

			self.validTimeLen += 1

		else:

			self.validTimeLen = 1

		self.lastTime = self.data.datetime.time(0).isoformat()

		if self.position:

			self.justEnteredOrderToClose = self.manageTrade()

		# Make sure I am either not in the market or I just closed my last
		# position, and that I can still make a trade today
		if ((not self.position or self.justEnteredOrderToClose) and
			not self.justEnteredOrderToCloseForTheDay and self.atr > 0 and
			self.validTimeLen >= 2 and
			self.data.datetime.time(0).isoformat() >=
				self.params.firstTimeOfEntry and
			self.data.datetime.time(0).isoformat() <=
				self.params.lastTimeOfEntry):

			if self.params.debugging:
				self.logCurrentBarStats()

			self.setUpOrderIfPossible()