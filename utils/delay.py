def timeDelay(targetWPM, numWords, numChars):
    inputDelay = 0.01
    totalInputDelay = inputDelay * numChars

    timeToTake = (numWords * 60) / targetWPM
    delay = (timeToTake - totalInputDelay) / numWords
    return delay