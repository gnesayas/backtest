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

	cerebroNFLX.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroNVDA.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroROKU.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroSQ.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)
	cerebroTSLA.addstrategy(TrendFollowingStrategy, displayingStrategyLogs=True)

	cerebroNFLX.addstrategy(MomentumStrategy, displayingStrategyLogs=True)
	cerebroNVDA.addstrategy(MomentumStrategy, displayingStrategyLogs=True)
	cerebroROKU.addstrategy(MomentumStrategy, displayingStrategyLogs=True)
	cerebroSQ.addstrategy(MomentumStrategy, displayingStrategyLogs=True)
	cerebroTSLA.addstrategy(MomentumStrategy, displayingStrategyLogs=True)

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