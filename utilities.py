def roundedNumber(num):
	return round(num, 2)

def roundTo4Decimals(num):
	return round(num, 4)

def roundToInt(num):
	return int(round(num))

def divide(num1, num2):
	if num2 != 0:
		return num1/num2
	if num1 > 0:
		return float("inf")
	return -float("inf")

def nearest10CentLevelBreak(price, positionIsLong):
	if price == float("inf") or price == -float("inf"):
		return price
	basisPoint = price*100
	if positionIsLong:
		while basisPoint % 10 != 0:
			basisPoint -= 1
		return roundedNumber(basisPoint/100 - 0.01)
	else:
		while basisPoint % 10 != 0:
			basisPoint += 1
		return roundedNumber(basisPoint/100 + 0.01)

def ensureNonNull(value, replacement):
	if value is None:
		return replacement
	return value

def getClosestPoint(currentPrice, priorDayHigh, priorDayLow, dailyOpen):
	if priorDayHigh == None or priorDayLow == None or currentPrice == dailyOpen:
		return dailyOpen
	elif currentPrice == priorDayHigh:
		return priorDayHigh
	elif currentPrice == priorDayLow:
		return priorDayLow
	elif dailyOpen > priorDayHigh:
		if currentPrice > dailyOpen:
			return dailyOpen
		if currentPrice > priorDayHigh:
			if (roundedNumber(dailyOpen - currentPrice) <=
				roundedNumber(currentPrice - priorDayHigh)):
				return dailyOpen
			return priorDayHigh
		if currentPrice < priorDayLow:
			return priorDayLow
		if (roundedNumber(currentPrice - priorDayLow) <=
			roundedNumber(priorDayHigh - currentPrice)):
			return priorDayLow
		return priorDayHigh
	elif dailyOpen == priorDayHigh:
		if (roundedNumber(abs(currentPrice - priorDayLow)) <
			roundedNumber(abs(priorDayHigh - currentPrice))):
			return priorDayLow
		return priorDayHigh
	elif dailyOpen > priorDayLow:
		if currentPrice > priorDayHigh:
			return priorDayHigh
		if currentPrice < priorDayLow:
			return priorDayLow
		if (roundedNumber(priorDayHigh - currentPrice) <=
			roundedNumber(abs(currentPrice - dailyOpen))):
			return priorDayHigh
		if (roundedNumber(currentPrice - priorDayLow) <=
			roundedNumber(abs(currentPrice - dailyOpen))):
			return priorDayLow
		return dailyOpen
	elif dailyOpen == priorDayLow:
		if (roundedNumber(abs(priorDayHigh - currentPrice)) <
			roundedNumber(abs(currentPrice - priorDayLow))):
			return priorDayHigh
		return priorDayLow
	else:
		if currentPrice < dailyOpen:
			return dailyOpen
		if currentPrice < priorDayLow:
			if (roundedNumber(currentPrice - dailyOpen) <=
				roundedNumber(priorDayLow - currentPrice)):
				return dailyOpen
			return priorDayLow
		if currentPrice > priorDayHigh:
			return priorDayHigh
		if (roundedNumber(priorDayHigh - currentPrice) <=
			roundedNumber(currentPrice - priorDayLow)):
			return priorDayHigh
		return priorDayLow

def getPotentialEntry(currentPrice, priorDayHigh, priorDayLow, dailyOpen,
						minRisk, entrySelectiveness, use10CentBreaks, positionIsLong):
	closestPricePoint = getClosestPoint(currentPrice, priorDayHigh, priorDayLow,
																	dailyOpen)
	if positionIsLong:
		if use10CentBreaks:
			potentialEntry = roundedNumber(nearest10CentLevelBreak(
											closestPricePoint, positionIsLong) +
																			minRisk)
		else:
			potentialEntry = roundedNumber(closestPricePoint - 0.01 + minRisk)
		if potentialEntry > currentPrice + entrySelectiveness:
			return potentialEntry
		return None
	else:
		if use10CentBreaks:
			potentialEntry = roundedNumber(nearest10CentLevelBreak(
											closestPricePoint, positionIsLong) -
																			minRisk)
		else:
			potentialEntry = roundedNumber(closestPricePoint + 0.01 - minRisk)
		if potentialEntry < currentPrice - entrySelectiveness:
			return potentialEntry
		return None

def getPotentialExit(currentPrice, priorDayHigh, priorDayLow, dailyOpen, highOfDay,
						lowOfDay, lastLocalHigh, lastLocalLow, currentBarHigh,
						currentBarLow, useDailyHighLowStops,useLocalVals, useCurrentBar,
						use10CentBreaks, positionIsLong):
	validRiskPoints = []
	if positionIsLong:
		if use10CentBreaks:
			priorDayHighBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayHigh, float("inf")),
										positionIsLong)
			priorDayLowBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayLow, float("inf")),
										positionIsLong)
			dailyOpenBreak = nearest10CentLevelBreak(
										ensureNonNull(dailyOpen, float("inf")),
										positionIsLong)
			lowOfDayBreak = nearest10CentLevelBreak(lowOfDay, positionIsLong)
			lastLocalLowBreak = nearest10CentLevelBreak(
										ensureNonNull(lastLocalLow, float("inf")),
										positionIsLong)
			currentBarLowBreak = nearest10CentLevelBreak(currentBarLow,
										positionIsLong)
		else:
			priorDayHighBreak = roundedNumber(
									ensureNonNull(priorDayHigh, float("inf")) - 0.01)
			priorDayLowBreak = roundedNumber(
									ensureNonNull(priorDayLow, float("inf")) - 0.01)
			dailyOpenBreak = roundedNumber(
									ensureNonNull(dailyOpen, float("inf")) - 0.01)
			lowOfDayBreak = roundedNumber(lowOfDay - 0.01)
			lastLocalLowBreak = roundedNumber(
									ensureNonNull(lastLocalLow, float("inf")) - 0.01)
			currentBarLowBreak = roundedNumber(currentBarLow - 0.01)
		if priorDayHighBreak < currentPrice:
			validRiskPoints.append(priorDayHighBreak)
		if priorDayLowBreak < currentPrice:
			validRiskPoints.append(priorDayLowBreak)
		if dailyOpenBreak < currentPrice:
			validRiskPoints.append(dailyOpenBreak)
		if useDailyHighLowStops and lowOfDayBreak < currentPrice:
			validRiskPoints.append(lowOfDayBreak)
		if useLocalVals and lastLocalLowBreak < currentPrice:
			validRiskPoints.append(lastLocalLowBreak)
		if useCurrentBar and currentBarLowBreak < currentPrice:
			validRiskPoints.append(currentBarLowBreak)
		if len(validRiskPoints) > 0:
			return max(validRiskPoints)
		return 0.01
	else:
		if use10CentBreaks:
			priorDayHighBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayHigh, -float("inf")),
										positionIsLong)
			priorDayLowBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayLow, -float("inf")),
										positionIsLong)
			dailyOpenBreak = nearest10CentLevelBreak(
										ensureNonNull(dailyOpen, -float("inf")),
										positionIsLong)
			highOfDayBreak = nearest10CentLevelBreak(highOfDay, positionIsLong)
			lastLocalHighBreak = nearest10CentLevelBreak(
										ensureNonNull(lastLocalHigh, -float("inf")),
										positionIsLong)
			currentBarHighBreak = nearest10CentLevelBreak(currentBarHigh,
										positionIsLong)
		else:
			priorDayHighBreak = roundedNumber(
									ensureNonNull(priorDayHigh, -float("inf")) + 0.01)
			priorDayLowBreak = roundedNumber(
									ensureNonNull(priorDayLow, -float("inf")) + 0.01)
			dailyOpenBreak = roundedNumber(
									ensureNonNull(dailyOpen, -float("inf")) + 0.01)
			highOfDayBreak = roundedNumber(highOfDay + 0.01)
			lastLocalHighBreak = roundedNumber(
									ensureNonNull(lastLocalHigh, -float("inf")) + 0.01)
			currentBarHighBreak = roundedNumber(currentBarHigh + 0.01)
		if priorDayHighBreak > currentPrice:
			validRiskPoints.append(priorDayHighBreak)
		if priorDayLowBreak > currentPrice:
			validRiskPoints.append(priorDayLowBreak)
		if dailyOpenBreak > currentPrice:
			validRiskPoints.append(dailyOpenBreak)
		if useDailyHighLowStops and highOfDayBreak > currentPrice:
			validRiskPoints.append(highOfDayBreak)
		if useLocalVals and lastLocalHighBreak > currentPrice:
			validRiskPoints.append(lastLocalHighBreak)
		if useCurrentBar and currentBarHighBreak > currentPrice:
			validRiskPoints.append(currentBarHighBreak)
		if len(validRiskPoints) > 0:
			return min(validRiskPoints)
		return float("inf")

def getFarthestGoodExit(maxRiskPercent, currentPrice, priorDayHigh, priorDayLow,
							dailyOpen, highOfDay, lowOfDay, lastLocalHigh,
							lastLocalLow, currentBarHigh, currentBarLow,
							use10CentBreaks, positionIsLong):
	validRiskPoints = []
	maxRisk = roundedNumber(currentPrice * maxRiskPercent / 100)
	if positionIsLong:
		if use10CentBreaks:
			priorDayHighBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayHigh, float("inf")),
										positionIsLong)
			priorDayLowBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayLow, float("inf")),
										positionIsLong)
			dailyOpenBreak = nearest10CentLevelBreak(
										ensureNonNull(dailyOpen, float("inf")),
										positionIsLong)
			lowOfDayBreak = nearest10CentLevelBreak(lowOfDay, positionIsLong)
			lastLocalLowBreak = nearest10CentLevelBreak(
										ensureNonNull(lastLocalLow, float("inf")),
										positionIsLong)
			currentBarLowBreak = nearest10CentLevelBreak(currentBarLow,
										positionIsLong)
		else:
			priorDayHighBreak = roundedNumber(
									ensureNonNull(priorDayHigh, float("inf")) - 0.01)
			priorDayLowBreak = roundedNumber(
									ensureNonNull(priorDayLow, float("inf")) - 0.01)
			dailyOpenBreak = roundedNumber(
									ensureNonNull(dailyOpen, float("inf")) - 0.01)
			lowOfDayBreak = roundedNumber(lowOfDay - 0.01)
			lastLocalLowBreak = roundedNumber(
									ensureNonNull(lastLocalLow, float("inf")) - 0.01)
			currentBarLowBreak = roundedNumber(currentBarLow - 0.01)
		if priorDayHighBreak < currentPrice and roundedNumber(currentPrice -
													priorDayHighBreak) <= maxRisk:
			validRiskPoints.append(priorDayHighBreak)
		if priorDayLowBreak < currentPrice and roundedNumber(currentPrice -
													priorDayLowBreak) <= maxRisk:
			validRiskPoints.append(priorDayLowBreak)
		if dailyOpenBreak < currentPrice and roundedNumber(currentPrice -
													dailyOpenBreak) <= maxRisk:
			validRiskPoints.append(dailyOpenBreak)
		if lowOfDayBreak < currentPrice and roundedNumber(currentPrice -
													lowOfDayBreak) <= maxRisk:
			validRiskPoints.append(lowOfDayBreak)
		if lastLocalLowBreak < currentPrice and roundedNumber(currentPrice -
													lastLocalLowBreak) <= maxRisk:
			validRiskPoints.append(lastLocalLowBreak)
		if currentBarLowBreak < currentPrice and roundedNumber(currentPrice -
													currentBarLowBreak) <= maxRisk:
			validRiskPoints.append(currentBarLowBreak)
		if len(validRiskPoints) > 0:
			return min(validRiskPoints)
		return 0.01
	else:
		if use10CentBreaks:
			priorDayHighBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayHigh, -float("inf")),
										positionIsLong)
			priorDayLowBreak = nearest10CentLevelBreak(
										ensureNonNull(priorDayLow, -float("inf")),
										positionIsLong)
			dailyOpenBreak = nearest10CentLevelBreak(
										ensureNonNull(dailyOpen, -float("inf")),
										positionIsLong)
			highOfDayBreak = nearest10CentLevelBreak(highOfDay, positionIsLong)
			lastLocalHighBreak = nearest10CentLevelBreak(
										ensureNonNull(lastLocalHigh, -float("inf")),
										positionIsLong)
			currentBarHighBreak = nearest10CentLevelBreak(currentBarHigh,
										positionIsLong)
		else:
			priorDayHighBreak = roundedNumber(
									ensureNonNull(priorDayHigh, -float("inf")) + 0.01)
			priorDayLowBreak = roundedNumber(
									ensureNonNull(priorDayLow, -float("inf")) + 0.01)
			dailyOpenBreak = roundedNumber(
									ensureNonNull(dailyOpen, -float("inf")) + 0.01)
			highOfDayBreak = roundedNumber(highOfDay + 0.01)
			lastLocalHighBreak = roundedNumber(
									ensureNonNull(lastLocalHigh, -float("inf")) + 0.01)
			currentBarHighBreak = roundedNumber(currentBarHigh + 0.01)
		if priorDayHighBreak > currentPrice and roundedNumber(priorDayHighBreak -
													currentPrice) <= maxRisk:
			validRiskPoints.append(priorDayHighBreak)
		if priorDayLowBreak > currentPrice and roundedNumber(priorDayLowBreak -
													currentPrice) <= maxRisk:
			validRiskPoints.append(priorDayLowBreak)
		if dailyOpenBreak > currentPrice and roundedNumber(dailyOpenBreak -
													currentPrice) <= maxRisk:
			validRiskPoints.append(dailyOpenBreak)
		if highOfDayBreak > currentPrice and roundedNumber(highOfDayBreak -
													currentPrice) <= maxRisk:
			validRiskPoints.append(highOfDayBreak)
		if lastLocalHighBreak > currentPrice and roundedNumber(lastLocalHighBreak -
													currentPrice) <= maxRisk:
			validRiskPoints.append(lastLocalHighBreak)
		if currentBarHighBreak > currentPrice and roundedNumber(currentBarHighBreak -
													currentPrice) <= maxRisk:
			validRiskPoints.append(currentBarHighBreak)
		if len(validRiskPoints) > 0:
			return max(validRiskPoints)
		return float("inf")

def getBarBasedExit(maxRiskPercent, currentPrice, recentPrices, stopWindowLen,
	use10CentBreaks, positionIsLong):
	start = len(recentPrices) - 1
	if positionIsLong:
		result = float("inf")
		for i in range(0, stopWindowLen):
			if recentPrices[start - i] < result:
				result = recentPrices[start - i]
		if use10CentBreaks:
			result = nearest10CentLevelBreak(result, positionIsLong)
		else:
			result = roundedNumber(result - 0.01)
		referencePoint = roundedNumber(currentPrice * (1 - maxRiskPercent/100))
		if result >= referencePoint:
			return result
		return 0.01
	else:
		result = -float("inf")
		for i in range(0, stopWindowLen):
			if recentPrices[start - i] > result:
				result = recentPrices[start - i]
		if use10CentBreaks:
			result = nearest10CentLevelBreak(result, positionIsLong)
		else:
			result = roundedNumber(result + 0.01)
		referencePoint = roundedNumber(currentPrice * (1 + maxRiskPercent/100))
		if result <= referencePoint:
			return result
		return float("inf")

def getPotentialStop(recentPrices, stopWindowLen, use10CentBreaks, positionIsLong):
	start = len(recentPrices) - 1
	if positionIsLong:
		result = float("inf")
		for i in range(0, stopWindowLen):
			if recentPrices[start - i] < result:
				result = recentPrices[start - i]
		if use10CentBreaks:
			result = nearest10CentLevelBreak(result, positionIsLong)
		else:
			result = roundedNumber(result - 0.01)
		return result
	else:
		result = -float("inf")
		for i in range(0, stopWindowLen):
			if recentPrices[start - i] > result:
				result = recentPrices[start - i]
		if use10CentBreaks:
			result = nearest10CentLevelBreak(result, positionIsLong)
		else:
			result = roundedNumber(result + 0.01)
		return result

def getNearestResistance(currentPrice, priorDayHigh, priorDayLow, dailyOpen,
							positionIsLong):
	validRewardPoints = []
	if positionIsLong:
		pHigh = ensureNonNull(priorDayHigh, -float("inf"))
		pLow = ensureNonNull(priorDayLow, -float("inf"))
		if pHigh > currentPrice:
			validRewardPoints.append(pHigh)
		if pLow > currentPrice:
			validRewardPoints.append(pLow)
		if dailyOpen > currentPrice:
			validRewardPoints.append(dailyOpen)
		if len(validRewardPoints) > 0:
			return min(validRewardPoints)
		return float("inf")
	else:
		pHigh = ensureNonNull(priorDayHigh, float("inf"))
		pLow = ensureNonNull(priorDayLow, float("inf"))
		if pHigh < currentPrice:
			validRewardPoints.append(pHigh)
		if pLow < currentPrice:
			validRewardPoints.append(pLow)
		if dailyOpen < currentPrice:
			validRewardPoints.append(dailyOpen)
		if len(validRewardPoints) > 0:
			return max(validRewardPoints)
		return 0.01

def getNearestInhibitingValues(potentialEntryPoint, entryLong=True):
	nearestWholeDollar = round(potentialEntryPoint)
	if entryLong:
		if nearestWholeDollar > potentialEntryPoint:
			return (nearestWholeDollar, nearestWholeDollar,
					(2*nearestWholeDollar - 1)/2 + 1)
		elif nearestWholeDollar < potentialEntryPoint:
			return (nearestWholeDollar, nearestWholeDollar + 1,
					(2*nearestWholeDollar + 1)/2)
		else:
			return (nearestWholeDollar, potentialEntryPoint + 1,
					potentialEntryPoint + 0.50)
	if nearestWholeDollar > potentialEntryPoint:
		return (nearestWholeDollar, nearestWholeDollar - 1,
				(2*nearestWholeDollar - 1)/2)
	elif nearestWholeDollar < potentialEntryPoint:
		return (nearestWholeDollar, nearestWholeDollar,
				(2*nearestWholeDollar + 1)/2 - 1)
	else:
		return (nearestWholeDollar, potentialEntryPoint - 1,
				potentialEntryPoint - 0.50)

def lastTimesValid(lastTime, currentTime, interval):
	(priorHour, priorMinute, zeros) = lastTime.split(":")
	(hour, minute, zeros) = currentTime.split(":")
	if (not((int(priorHour) == int(hour) and int(priorMinute) == int(minute) - interval) or
			(int(priorHour) == int(hour) - 1 and int(priorMinute) == 60 - interval))):
		return False
	return True

def getMaxAdverseExcursion(prices, windowLen, positionIsLong):
	if positionIsLong:
		result = float("inf")
		for i in range(windowLen):
			if prices[-i] < result:
				result = prices[-i]
		return result
	else:
		result = -float("inf")
		for i in range(windowLen):
			if prices[-i] > result:
				result = prices[-i]
		return result