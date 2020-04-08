import backtrader as bt

from utilities import *

# Create a Strategy
class MeanReversionStrategy(bt.Strategy):

	params = (
		('firstTimeOfEntry', '08:30:00'),
		('lastTimeOfEntry', '09:29:00'),
		('maPeriod', 20),
		('goodCandlesBeforeEntry', 2),
		('atrRiskDenominator', 10),
		('minRRratio', 3),
		('consecutiveGoodCandles', 3),
		('debugging', False),
		('displayingStrategyLogs', False)
	)

	'''

-------------------- Backtest Results --------------------

firstTimeOfEntry: 08:45:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 2 consecutiveGoodCandles: 5
Trades: 25 winrate: 24.0% averageSize: 109.9200 centsPerWin: 287.1571 centsPerLoss: 54.5690 profitLossRatio: 5.2623 expectancy: 0.2745 PnL: 754.1963
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 2 consecutiveGoodCandles: 5
Trades: 25 winrate: 24.0% averageSize: 109.9200 centsPerWin: 287.1571 centsPerLoss: 54.5690 profitLossRatio: 5.2623 expectancy: 0.2745 PnL: 754.1963
firstTimeOfEntry: 08:40:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 2 consecutiveGoodCandles: 5
Trades: 26 winrate: 23.0769% averageSize: 109.8077 centsPerWin: 287.4508 centsPerLoss: 54.6220 profitLossRatio: 5.2625 expectancy: 0.2432 PnL: 694.2763
firstTimeOfEntry: 08:40:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 12 winrate: 25.0% averageSize: 100.0833 centsPerWin: 393.9484 centsPerLoss: 59.8512 profitLossRatio: 6.5821 expectancy: 0.5360 PnL: 643.7205
firstTimeOfEntry: 08:45:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 12 winrate: 25.0% averageSize: 100.0833 centsPerWin: 393.9484 centsPerLoss: 59.8512 profitLossRatio: 6.5821 expectancy: 0.5360 PnL: 643.7205
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 12 winrate: 25.0% averageSize: 100.0833 centsPerWin: 393.9484 centsPerLoss: 59.8512 profitLossRatio: 6.5821 expectancy: 0.5360 PnL: 643.7205
firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 2 consecutiveGoodCandles: 5
Trades: 27 winrate: 22.2222% averageSize: 108.5185 centsPerWin: 290.8657 centsPerLoss: 55.8971 profitLossRatio: 5.2036 expectancy: 0.2116 PnL: 620.0263
firstTimeOfEntry: 08:35:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 2 consecutiveGoodCandles: 5
Trades: 27 winrate: 22.2222% averageSize: 108.5185 centsPerWin: 290.8657 centsPerLoss: 55.8971 profitLossRatio: 5.2036 expectancy: 0.2116 PnL: 620.0263
firstTimeOfEntry: 08:40:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 441.1781 centsPerLoss: 55.8084 profitLossRatio: 7.9052 expectancy: 0.6844 PnL: 587.8844
firstTimeOfEntry: 08:45:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 441.1781 centsPerLoss: 55.8084 profitLossRatio: 7.9052 expectancy: 0.6844 PnL: 587.8844
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 441.1781 centsPerLoss: 55.8084 profitLossRatio: 7.9052 expectancy: 0.6844 PnL: 587.8844
firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 13 winrate: 23.0769% averageSize: 98.1538 centsPerWin: 401.6925 centsPerLoss: 62.4896 profitLossRatio: 6.4281 expectancy: 0.4463 PnL: 569.4705

firstTimeOfEntry: 08:40:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 441.1781 centsPerLoss: 55.8084 profitLossRatio: 7.9052 PnL: 587.8844 expectancy: 0.6844
firstTimeOfEntry: 08:45:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 441.1781 centsPerLoss: 55.8084 profitLossRatio: 7.9052 PnL: 587.8844 expectancy: 0.6844
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 441.1781 centsPerLoss: 55.8084 profitLossRatio: 7.9052 PnL: 587.8844 expectancy: 0.6844
firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 9 winrate: 22.2222% averageSize: 103.7778 centsPerWin: 456.4706 centsPerLoss: 59.7149 profitLossRatio: 7.6442 PnL: 513.6344 expectancy: 0.5499
firstTimeOfEntry: 08:35:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 5
Trades: 9 winrate: 22.2222% averageSize: 103.7778 centsPerWin: 456.4706 centsPerLoss: 59.7149 profitLossRatio: 7.6442 PnL: 513.6344 expectancy: 0.5499
firstTimeOfEntry: 08:40:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 12 winrate: 25.0% averageSize: 100.0833 centsPerWin: 393.9484 centsPerLoss: 59.8512 profitLossRatio: 6.5821 PnL: 643.7205 expectancy: 0.5360
firstTimeOfEntry: 08:45:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 12 winrate: 25.0% averageSize: 100.0833 centsPerWin: 393.9484 centsPerLoss: 59.8512 profitLossRatio: 6.5821 PnL: 643.7205 expectancy: 0.5360
firstTimeOfEntry: 08:50:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 12 winrate: 25.0% averageSize: 100.0833 centsPerWin: 393.9484 centsPerLoss: 59.8512 profitLossRatio: 6.5821 PnL: 643.7205 expectancy: 0.5360
firstTimeOfEntry: 08:30:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 13 winrate: 23.0769% averageSize: 98.1538 centsPerWin: 401.6925 centsPerLoss: 62.4896 profitLossRatio: 6.4281 PnL: 569.4705 expectancy: 0.4463
firstTimeOfEntry: 08:35:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 3 consecutiveGoodCandles: 5
Trades: 13 winrate: 23.0769% averageSize: 98.1538 centsPerWin: 401.6925 centsPerLoss: 62.4896 profitLossRatio: 6.4281 PnL: 569.4705 expectancy: 0.4463
firstTimeOfEntry: 08:40:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 4
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 344.8289 centsPerLoss: 55.8084 profitLossRatio: 6.1788 PnL: 380.9744 expectancy: 0.4435
firstTimeOfEntry: 08:45:00 lastTimeOfEntry: 09:29:00 maPeriod: 20 goodCandlesBeforeEntry: 2 atrRiskDenominator: 10 minRRratio: 4 consecutiveGoodCandles: 4
Trades: 8 winrate: 25.0% averageSize: 107.3750 centsPerWin: 344.8289 centsPerLoss: 55.8084 profitLossRatio: 6.1788 PnL: 380.9744 expectancy: 0.4435

	'''

	maxRiskPerTrade = 60.00

	endOfSession = '14:58:00'

	backupFileName = 'backupMrevResults.txt'
	filename = 'mrevResults.txt'

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
		self.lastTime = None
		self.validTimeLen = 1
		self.countingGreenBars = False
		self.countingRedBars = False
		self.greenBarCount = 0
		self.redBarCount = 0
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

	def logDecisionMetrics(self, entry, exit, positionIsLong):
		if positionIsLong:
			self.log('Entry Long: ' + str(entry)
						+ ' Stop: ' + str(exit))
		else:
			self.log('Entry Short: ' + str(entry)
						+ ' Stop: ' + str(exit))

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

				if (roundedNumber(self.dataclose[0]) >
					roundedNumber(self.dataopen[0])):

					self.consecutiveBarCounter += 1

				else:

					self.consecutiveBarCounter = 0

				if (self.consecutiveBarCounter ==
					self.params.consecutiveGoodCandles):

					if (roundedNumber(self.dataclose[0]) > self.lastGoodPrice or
						(self.data.datetime.time(0).isoformat() <
							self.params.lastTimeOfEntry and
						self.validTimeLen >= 2 and
						self.greenBarCount ==
							self.params.goodCandlesBeforeEntry and
						roundedNumber(self.dataclose[0] - self.currentDayLow) <=
							self.dollarRisk and
						roundedNumber((self.vwap - self.dataclose[0])/
							(self.dataclose[0] - self.currentDayLow)) >=
							self.params.minRRratio
						)):

						self.consecutiveBarCounter = 0
						self.lastGoodPrice = roundedNumber(self.dataclose[0])

					else:

						if self.params.debugging:
							self.log(str(self.params.consecutiveGoodCandles)
								+ ' consecutive good candles closed equal to or'
								+ ' lower than the same price as my long entry,'
								+ ' or the last time this happened, exiting now')
							self.log('Ref of order to be cancelled: '
								+ str(self.currentStopOrder.ref))

						self.cancel(self.currentStopOrder)

						self.close()

						return True

			else:

				if (roundedNumber(self.dataclose[0]) <
					roundedNumber(self.dataopen[0])):

					self.consecutiveBarCounter += 1

				else:

					self.consecutiveBarCounter = 0

				if (self.consecutiveBarCounter ==
					self.params.consecutiveGoodCandles):

					if (roundedNumber(self.dataclose[0]) < self.lastGoodPrice or
						(self.data.datetime.time(0).isoformat() <
							self.params.lastTimeOfEntry and
						self.validTimeLen >= 2 and
						self.redBarCount ==
							self.params.goodCandlesBeforeEntry and
						roundedNumber(self.currentDayHigh - self.dataclose[0]) <=
							self.dollarRisk and
						roundedNumber((self.dataclose[0] - self.vwap)/
							(self.currentDayHigh - self.dataclose[0])) >=
							self.params.minRRratio
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

		if (self.greenBarCount == self.params.goodCandlesBeforeEntry and
			roundedNumber(self.dataclose[0] - self.currentDayLow) <=
				self.dollarRisk and
			roundedNumber((self.vwap - self.dataclose[0])/
				(self.dataclose[0] - self.currentDayLow)) >=
				self.params.minRRratio
			):

			self.potentialEntryLong = roundedNumber(self.dataclose[0])
			self.potentialExitFromLong = roundedNumber(self.potentialEntryLong -
														self.dollarRisk)

			if self.params.displayingStrategyLogs:
				self.log('ENTERING MARKET ORDER LONG')
				self.logDecisionMetrics(self.potentialEntryLong,
										self.potentialExitFromLong, True)

			self.currentMarketOrder = self.buy(
											size=self.initialSize,
											exectype=bt.Order.Market,
											valid=bt.Order.DAY)

			return

		####### See if I have a setup to go Short #######

		if (self.redBarCount == self.params.goodCandlesBeforeEntry and
			roundedNumber(self.currentDayHigh - self.dataclose[0]) <=
				self.dollarRisk and
			roundedNumber((self.dataclose[0] - self.vwap)/
				(self.currentDayHigh - self.dataclose[0])) >=
				self.params.minRRratio
			):

			self.potentialEntryShort = roundedNumber(self.dataclose[0])
			self.potentialExitFromShort = roundedNumber(
													self.potentialEntryShort +
													self.dollarRisk)

			if self.params.displayingStrategyLogs:
				self.log('ENTERING MARKET ORDER SHORT')
				self.logDecisionMetrics(self.potentialEntryShort,
									self.potentialExitFromShort, False)

			self.currentMarketOrder = self.sell(
											size=self.initialSize,
											exectype=bt.Order.Market,
											valid=bt.Order.DAY)

			return

	def calculateATR(self):
		diffs = []
		diffs.append(roundedNumber(abs(self.currentDayHigh -
										self.dailyCloses[-1])))
		diffs.append(roundedNumber(abs(self.currentDayLow -
										self.dailyCloses[-1])))
		diffs.append(roundedNumber(self.currentDayHigh - self.currentDayLow))
		self.atrSum += max(diffs)
		self.atr = roundedNumber(self.atrSum/len(self.dailyCloses))

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
			self.countingGreenBars = False
			self.countingRedBars = False
			self.greenBarCount = 0
			self.redBarCount = 0
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
			self.countingRedBars = False

		if roundedNumber(self.datalow[0]) < self.currentDayLow:

			self.currentDayLow = roundedNumber(self.datalow[0])
			self.countingGreenBars = False

		if (self.lastTime != None and lastTimesValid(self.lastTime,
			self.data.datetime.time(0).isoformat(), 1)):

			self.validTimeLen += 1

		else:

			self.validTimeLen = 1

		self.lastTime = self.data.datetime.time(0).isoformat()

		if roundedNumber(self.dataclose[0]) < roundedNumber(self.dataopen[0]):

			if self.currentDayLow != roundedNumber(self.datalow[0]):

				self.countingGreenBars = True

			self.greenBarCount = 0

			if self.countingRedBars:

				if self.currentDayHigh == roundedNumber(self.datahigh[0]):

					self.redBarCount = 0

				else:

					self.redBarCount += 1

		elif roundedNumber(self.dataclose[0]) > roundedNumber(self.dataopen[0]):

			if self.currentDayHigh != roundedNumber(self.datahigh[0]):

				self.countingRedBars = True

			self.redBarCount = 0

			if self.countingGreenBars:

				if self.currentDayLow == roundedNumber(self.datalow[0]):

					self.greenBarCount = 0

				else:

					self.greenBarCount += 1

		else:

			self.greenBarCount = 0
			self.redBarCount = 0

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