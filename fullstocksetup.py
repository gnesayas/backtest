	dataAAPL = MyDataFeed(dataname='data/MY_intraday_1min_AAPL.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataAMD = MyDataFeed(dataname='data/MY_intraday_1min_AMD.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataBA = MyDataFeed(dataname='data/MY_intraday_1min_BA.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataBABA = MyDataFeed(dataname='data/MY_intraday_1min_BABA.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataC = MyDataFeed(dataname='data/MY_intraday_1min_C.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataCSCO = MyDataFeed(dataname='data/MY_intraday_1min_CSCO.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataDIS = MyDataFeed(dataname='data/MY_intraday_1min_DIS.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataFB = MyDataFeed(dataname='data/MY_intraday_1min_FB.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataINTC = MyDataFeed(dataname='data/MY_intraday_1min_INTC.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataJPM = MyDataFeed(dataname='data/MY_intraday_1min_JPM.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataMO = MyDataFeed(dataname='data/MY_intraday_1min_MO.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataMSFT = MyDataFeed(dataname='data/MY_intraday_1min_MSFT.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataMU = MyDataFeed(dataname='data/MY_intraday_1min_MU.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataNFLX = MyDataFeed(dataname='data/MY_intraday_1min_NFLX.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataNVDA = MyDataFeed(dataname='data/MY_intraday_1min_NVDA.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataOXY = MyDataFeed(dataname='data/MY_intraday_1min_OXY.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataPINS = MyDataFeed(dataname='data/MY_intraday_1min_PINS.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataQCOM = MyDataFeed(dataname='data/MY_intraday_1min_QCOM.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataROKU = MyDataFeed(dataname='data/MY_intraday_1min_ROKU.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataSCHW = MyDataFeed(dataname='data/MY_intraday_1min_SCHW.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataSLB = MyDataFeed(dataname='data/MY_intraday_1min_SLB.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataSQ = MyDataFeed(dataname='data/MY_intraday_1min_SQ.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataTSLA = MyDataFeed(dataname='data/MY_intraday_1min_TSLA.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataTWTR = MyDataFeed(dataname='data/MY_intraday_1min_TWTR.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataUBER = MyDataFeed(dataname='data/MY_intraday_1min_UBER.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataUGAZ = MyDataFeed(dataname='data/MY_intraday_1min_UGAZ.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataWORK = MyDataFeed(dataname='data/MY_intraday_1min_WORK.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)
	dataXOM = MyDataFeed(dataname='data/MY_intraday_1min_XOM.csv',
						timeframe=bt.TimeFrame.Minutes, compression=1)

	cerebroAAPL = bt.Cerebro()
	cerebroAMD = bt.Cerebro()
	cerebroBA = bt.Cerebro()
	cerebroBABA = bt.Cerebro()
	cerebroC = bt.Cerebro()
	cerebroCSCO = bt.Cerebro()
	cerebroDIS = bt.Cerebro()
	cerebroFB = bt.Cerebro()
	cerebroINTC = bt.Cerebro()
	cerebroJPM = bt.Cerebro()
	cerebroMO = bt.Cerebro()
	cerebroMSFT = bt.Cerebro()
	cerebroMU = bt.Cerebro()
	cerebroNFLX = bt.Cerebro()
	cerebroNVDA = bt.Cerebro()
	cerebroOXY = bt.Cerebro()
	cerebroPINS = bt.Cerebro()
	cerebroQCOM = bt.Cerebro()
	cerebroROKU = bt.Cerebro()
	cerebroSCHW = bt.Cerebro()
	cerebroSLB = bt.Cerebro()
	cerebroSQ = bt.Cerebro()
	cerebroTSLA = bt.Cerebro()
	cerebroTWTR = bt.Cerebro()
	cerebroUBER = bt.Cerebro()
	cerebroUGAZ = bt.Cerebro()
	cerebroWORK = bt.Cerebro()
	cerebroXOM = bt.Cerebro()

	cerebroAAPL.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroAMD.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroBA.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroBABA.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroC.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroCSCO.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroDIS.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroFB.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroINTC.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroJPM.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroMO.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroMSFT.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroMU.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroNFLX.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroNVDA.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroOXY.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroPINS.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroQCOM.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroROKU.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroSCHW.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroSLB.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroSQ.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroTSLA.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroTWTR.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroUBER.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroUGAZ.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroWORK.addanalyzer(TradeAnalyzer, _name='ta')
	cerebroXOM.addanalyzer(TradeAnalyzer, _name='ta')

	cerebroAAPL.broker.setcash(100000.0)
	cerebroAMD.broker.setcash(100000.0)
	cerebroBA.broker.setcash(100000.0)
	cerebroBABA.broker.setcash(100000.0)
	cerebroC.broker.setcash(100000.0)
	cerebroCSCO.broker.setcash(100000.0)
	cerebroDIS.broker.setcash(100000.0)
	cerebroFB.broker.setcash(100000.0)
	cerebroINTC.broker.setcash(100000.0)
	cerebroJPM.broker.setcash(100000.0)
	cerebroMO.broker.setcash(100000.0)
	cerebroMSFT.broker.setcash(100000.0)
	cerebroMU.broker.setcash(100000.0)
	cerebroNFLX.broker.setcash(100000.0)
	cerebroNVDA.broker.setcash(100000.0)
	cerebroOXY.broker.setcash(100000.0)
	cerebroPINS.broker.setcash(100000.0)
	cerebroQCOM.broker.setcash(100000.0)
	cerebroROKU.broker.setcash(100000.0)
	cerebroSCHW.broker.setcash(100000.0)
	cerebroSLB.broker.setcash(100000.0)
	cerebroSQ.broker.setcash(100000.0)
	cerebroTSLA.broker.setcash(100000.0)
	cerebroTWTR.broker.setcash(100000.0)
	cerebroUBER.broker.setcash(100000.0)
	cerebroUGAZ.broker.setcash(100000.0)
	cerebroWORK.broker.setcash(100000.0)
	cerebroXOM.broker.setcash(100000.0)
	
	cerebroAAPL.broker.addcommissioninfo(comminfo)
	cerebroAMD.broker.addcommissioninfo(comminfo)
	cerebroBA.broker.addcommissioninfo(comminfo)
	cerebroBABA.broker.addcommissioninfo(comminfo)
	cerebroC.broker.addcommissioninfo(comminfo)
	cerebroCSCO.broker.addcommissioninfo(comminfo)
	cerebroDIS.broker.addcommissioninfo(comminfo)
	cerebroFB.broker.addcommissioninfo(comminfo)
	cerebroINTC.broker.addcommissioninfo(comminfo)
	cerebroJPM.broker.addcommissioninfo(comminfo)
	cerebroMO.broker.addcommissioninfo(comminfo)
	cerebroMSFT.broker.addcommissioninfo(comminfo)
	cerebroMU.broker.addcommissioninfo(comminfo)
	cerebroNFLX.broker.addcommissioninfo(comminfo)
	cerebroNVDA.broker.addcommissioninfo(comminfo)
	cerebroOXY.broker.addcommissioninfo(comminfo)
	cerebroPINS.broker.addcommissioninfo(comminfo)
	cerebroQCOM.broker.addcommissioninfo(comminfo)
	cerebroROKU.broker.addcommissioninfo(comminfo)
	cerebroSCHW.broker.addcommissioninfo(comminfo)
	cerebroSLB.broker.addcommissioninfo(comminfo)
	cerebroSQ.broker.addcommissioninfo(comminfo)
	cerebroTSLA.broker.addcommissioninfo(comminfo)
	cerebroTWTR.broker.addcommissioninfo(comminfo)
	cerebroUBER.broker.addcommissioninfo(comminfo)
	cerebroUGAZ.broker.addcommissioninfo(comminfo)
	cerebroWORK.broker.addcommissioninfo(comminfo)
	cerebroXOM.broker.addcommissioninfo(comminfo)

	cerebroAAPL.adddata(dataAAPL)
	cerebroAMD.adddata(dataAMD)
	cerebroBA.adddata(dataBA)
	cerebroBABA.adddata(dataBABA)
	cerebroC.adddata(dataC)
	cerebroCSCO.adddata(dataCSCO)
	cerebroDIS.adddata(dataDIS)
	cerebroFB.adddata(dataFB)
	cerebroINTC.adddata(dataINTC)
	cerebroJPM.adddata(dataJPM)
	cerebroMO.adddata(dataMO)
	cerebroMSFT.adddata(dataMSFT)
	cerebroMU.adddata(dataMU)
	cerebroNFLX.adddata(dataNFLX)
	cerebroNVDA.adddata(dataNVDA)
	cerebroOXY.adddata(dataOXY)
	cerebroPINS.adddata(dataPINS)
	cerebroQCOM.adddata(dataQCOM)
	cerebroROKU.adddata(dataROKU)
	cerebroSCHW.adddata(dataSCHW)
	cerebroSLB.adddata(dataSLB)
	cerebroSQ.adddata(dataSQ)
	cerebroTSLA.adddata(dataTSLA)
	cerebroTWTR.adddata(dataTWTR)
	cerebroUBER.adddata(dataUBER)
	cerebroUGAZ.adddata(dataUGAZ)
	cerebroWORK.adddata(dataWORK)
	cerebroXOM.adddata(dataXOM)

	cerebroAAPL.addstrategy(MyBestStrategy)
	cerebroAMD.addstrategy(MyBestStrategy)
	cerebroBA.addstrategy(MyBestStrategy)
	cerebroBABA.addstrategy(MyBestStrategy)
	cerebroC.addstrategy(MyBestStrategy)
	cerebroCSCO.addstrategy(MyBestStrategy)
	cerebroDIS.addstrategy(MyBestStrategy)
	cerebroFB.addstrategy(MyBestStrategy)
	cerebroINTC.addstrategy(MyBestStrategy)
	cerebroJPM.addstrategy(MyBestStrategy)
	cerebroMO.addstrategy(MyBestStrategy)
	cerebroMSFT.addstrategy(MyBestStrategy)
	cerebroMU.addstrategy(MyBestStrategy)
	cerebroNFLX.addstrategy(MyBestStrategy)
	cerebroNVDA.addstrategy(MyBestStrategy)
	cerebroOXY.addstrategy(MyBestStrategy)
	cerebroPINS.addstrategy(MyBestStrategy)
	cerebroQCOM.addstrategy(MyBestStrategy)
	cerebroROKU.addstrategy(MyBestStrategy)
	cerebroSCHW.addstrategy(MyBestStrategy)
	cerebroSLB.addstrategy(MyBestStrategy)
	cerebroSQ.addstrategy(MyBestStrategy)
	cerebroTSLA.addstrategy(MyBestStrategy)
	cerebroTWTR.addstrategy(MyBestStrategy)
	cerebroUBER.addstrategy(MyBestStrategy)
	cerebroUGAZ.addstrategy(MyBestStrategy)
	cerebroWORK.addstrategy(MyBestStrategy)
	cerebroXOM.addstrategy(MyBestStrategy)
	
	aaplStrat = cerebroAAPL.run()[0]
	amdStrat = cerebroAMD.run()[0]
	baStrat = cerebroBA.run()[0]
	babaStrat = cerebroBABA.run()[0]
	cStrat = cerebroC.run()[0]
	cscoStrat = cerebroCSCO.run()[0]
	disStrat = cerebroDIS.run()[0]
	fbStrat = cerebroFB.run()[0]
	intcStrat = cerebroINTC.run()[0]
	jpmStrat = cerebroJPM.run()[0]
	moStrat = cerebroMO.run()[0]
	msftStrat = cerebroMSFT.run()[0]
	muStrat = cerebroMU.run()[0]
	nflxStrat = cerebroNFLX.run()[0]
	nvdaStrat = cerebroNVDA.run()[0]
	oxyStrat = cerebroOXY.run()[0]
	pinsStrat = cerebroPINS.run()[0]
	qcomStrat = cerebroQCOM.run()[0]
	rokuStrat = cerebroROKU.run()[0]
	schwStrat = cerebroSCHW.run()[0]
	slbStrat = cerebroSLB.run()[0]
	sqStrat = cerebroSQ.run()[0]
	tslaStrat = cerebroTSLA.run()[0]
	twtrStrat = cerebroTWTR.run()[0]
	uberStrat = cerebroUBER.run()[0]
	ugazStrat = cerebroUGAZ.run()[0]
	workStrat = cerebroWORK.run()[0]
	xomStrat = cerebroXOM.run()[0]

	analyzerList = [
					aaplStrat.analyzers.ta,
					amdStrat.analyzers.ta,
					baStrat.analyzers.ta,
					babaStrat.analyzers.ta,
					cStrat.analyzers.ta,
					cscoStrat.analyzers.ta,
					disStrat.analyzers.ta,
					fbStrat.analyzers.ta,
					intcStrat.analyzers.ta,
					jpmStrat.analyzers.ta,
					moStrat.analyzers.ta,
					msftStrat.analyzers.ta,
					muStrat.analyzers.ta,
					nflxStrat.analyzers.ta,
					nvdaStrat.analyzers.ta,
					oxyStrat.analyzers.ta,
					pinsStrat.analyzers.ta,
					qcomStrat.analyzers.ta,
					rokuStrat.analyzers.ta,
					schwStrat.analyzers.ta,
					slbStrat.analyzers.ta,
					sqStrat.analyzers.ta,
					tslaStrat.analyzers.ta,
					twtrStrat.analyzers.ta,
					uberStrat.analyzers.ta,
					workStrat.analyzers.ta,
					xomStrat.analyzers.ta
	]