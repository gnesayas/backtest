import backtrader as bt

from utilities import *

class TradeAnalyzer(bt.Analyzer):

	def __init__(self):
		self.tradeCount = 0

		self.wins = 0
		self.losses = 0
		self.totalSharesTraded = 0
		self.totalProfits = 0.0
		self.totalLosses = 0.0
		self.pnl = 0.0
		
		self.winrate = 0.0
		self.averageShareSize = 0.0
		self.centsPerWin = 0.0
		self.centsPerLoss = 0.0
		self.profitLossRatio = 0.0
		self.expectancy = 0.0

	def notify_trade(self, trade):
		if not trade.isclosed:
			return

		self.tradeCount += 1

		self.pnl += trade.pnl
		self.totalSharesTraded += self.strategy.initialSize

		if trade.pnl > 0:
			self.wins += 1
			self.totalProfits += trade.pnl*100
			self.centsPerWin = self.totalProfits/self.wins
		else:
			self.losses += 1
			self.totalLosses -= trade.pnl*100
			self.centsPerLoss = self.totalLosses/self.losses

		self.winrate = self.wins*100/self.tradeCount
		self.averageShareSize = self.totalSharesTraded/self.tradeCount

		if self.centsPerLoss == 0.0:
			self.profitLossRatio = float("inf")
		else:
			self.profitLossRatio = self.centsPerWin/self.centsPerLoss

		self.expectancy = self.pnl/self.averageShareSize/self.tradeCount

	def get_analysis(self):
		return (
			('Wins', self.wins),
			('Losses', self.losses),
			('Win Rate', str(roundTo4Decimals(self.winrate)) + "%"),
			('Cents per Win', roundTo4Decimals(self.centsPerWin)),
			('Cents per Loss', roundTo4Decimals(self.centsPerLoss)),
			('Profit/Loss Ratio', roundTo4Decimals(self.profitLossRatio)),
			('Trade Expectancy', roundTo4Decimals(self.expectancy)),
			('PnL', roundTo4Decimals(self.pnl))
		)

	def stop(self):
		with open(self.strategy.filename, "a") as f:
			f.write('RESULT: ' + str(self.strategy.broker.getvalue()) + "\n")
			f.write(str(self.get_analysis()))

		print('RESULT: ' + str(self.strategy.broker.getvalue()))
		self.pprint()