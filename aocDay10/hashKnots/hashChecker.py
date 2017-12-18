'''
Created on Dec 10, 2017

@author: Zog
'''
def hash_checker(inputString):
    baseChars = []
    for i in inputString:
        baseChars.append(ord(i))
    part2Appendix = [17, 31, 73, 47, 23]
    workingLengths = baseChars + part2Appendix
    skipSpan = 0
    listPosition = 0
    numList = list(range(256))
    sublist = []
    
    workingList = numList
    listLen = len(workingList)
    
    for x in range(64):
        for i in workingLengths:
            if listPosition + i > listLen:
                subListIdices = list(range(listPosition%listLen, listLen))
                for k in range((listPosition+i)%listLen):
                    subListIdices.append(k)
            else:
                subListIdices = list(range(listPosition, listPosition + i))
            for j in subListIdices:
                index = j%listLen
                sublist.append(workingList[index])
            for j in subListIdices:
                workingList[j] = sublist.pop()
            listPosition = (listPosition + i + skipSpan)%listLen
            skipSpan = skipSpan + 1
    
    rawDenseHash = []
    for i in range(16):
        denseEntry = 0
        for j in range(16):
            base = i * 16
            index = j + base
            denseEntry = denseEntry ^ workingList[index]
        rawDenseHash.append(denseEntry)
    
    hexDenseHash = ""
    for i in rawDenseHash:
        hexString = format(i,'x')
        if len(hexString) == 1:
            hexString = '0' + hexString
        hexDenseHash = hexDenseHash + hexString                
    
    print("Final hex hash: " + hexDenseHash)
        
    checksum = workingList[0] * workingList[1]
    print("Product of first two elements: " + str(checksum))
    return hexDenseHash

if __name__ == '__main__':
    baseLengthsChars = "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243"
    testHash = "102,108,113,114,103,110,107,120,045,048"
    hash_checker(baseLengthsChars)
#     hash_checker(testHash)
    
    pass