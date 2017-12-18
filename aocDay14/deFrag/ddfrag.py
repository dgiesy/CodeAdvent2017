'''
Created on Dec 16, 2017

@author: Zog
'''

from hashKnots.hashChecker import hash_checker

def asciiToDecimal(textString):
    asciiNumString = ""
    for i in textString:
        if len(asciiNumString) == 0:
            asciiNumString = str(ord(i))
        else:
            asciiNumString = asciiNumString + "," + str(ord(i))
        
    return asciiNumString

def hex_to_bin(hexVersion):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 4
    binVersionString = ""
    binArr = []
    for i in hexVersion:
        binary = bin(int(i, scale))[2:].zfill(num_of_bits)
        binVersionString = binVersionString + binary
        binArr.append(binary)
    
    return binVersionString, binArr

def update_first_row(firstRow,groupSeed):
    currentGroup = groupSeed
    lastGroup = groupSeed - 1
    inGroup = False
    
    cells = len(firstRow)
    for i in range(cells):
        if firstRow[i] == '0':
            if inGroup:
                currentGroup += 1
            inGroup = False
            continue
        if i == 0:
            inGroup = True
            continue
        previousIndex = i - 1
        previousCellValue = firstRow[previousIndex]
        currentCellValue = firstRow[i]
        if int(previousCellValue) == 1:
            continue
        elif int(previousCellValue) > 1:
            if int(currentCellValue) > 1:
                prevailingValue = str(min(int(previousCellValue),int(currentCellValue)))
            else:
                prevailingValue =  previousCellValue
            firstRow[previousIndex] = prevailingValue
            firstRow[i] = prevailingValue
            inGroup = True
        elif int(firstRow[i]) > 1:
            continue
        else:
            firstRow[i] = str(currentGroup)
            lastGroup = currentGroup
            inGroup = True
#     print("Last Group: " + str(lastGroup))
#     print("Current Group: " + str(currentGroup))
    if lastGroup == currentGroup:
        currentGroup += 1
    return firstRow, currentGroup

def compare_with_above(top, bottom, nextGroup):
    changedTop = False
    topCopy = top[:]
    bottomCopy = bottom[:]
    cells = len(bottomCopy)
    inGroup = False
    incGroup = False
    for j in range(cells):
        if bottomCopy[j] == "0":
            if inGroup and incGroup:
                nextGroup += 1
                incGroup = False
            inGroup = False
            continue
        if j == 0:
    #             No last cell
            nextGroup += 1
            inGroup = True
            cellAbove = int(topCopy[j])
            if cellAbove > 0:
                bottomCopy[j] = str(cellAbove)
                incGroup = False
                continue
            else:
                bottomCopy[j] = str(nextGroup)
                incGroup = True
                continue
        else:
            inGroup = True
            cellAbove = int(topCopy[j])
            lastCell = int(bottomCopy[j - 1])
            if cellAbove > 0:
                if lastCell == 0:
                    bottomCopy[j] = str(cellAbove)
                    incGroup = False
                    continue
                if lastCell == 1:
                    bottomCopy[j - 1] = str(cellAbove)
                    bottomCopy[j] = str(cellAbove)
                    incGroup = False
                    continue
                if lastCell > 1:
                    prevailingGroup = min(lastCell, cellAbove)
                    topCopy[j] = str(prevailingGroup)
                    bottomCopy[j - 1] = str(prevailingGroup)
                    bottomCopy[j] = str(prevailingGroup)
                    incGroup = False
                    continue
            elif lastCell > 0:
                if lastCell == 1:
                    prevailingGroup = nextGroup
                    bottomCopy[j - 1] = str(prevailingGroup)
                    bottomCopy[j] = str(prevailingGroup)
                    incGroup = True
                    continue
                else:
                    bottomCopy[j] = str(lastCell)
                    incGroup = False
                    continue
            elif bottomCopy[j] == "1":
                bottomCopy[j] = str(nextGroup)
                incGroup = True
    return topCopy, bottomCopy, nextGroup

def convert_to_groups(matrix):
    inGroup = False
    incGroup = False
    
    stringRows = len(matrix)
    matrix[0], currentGroup = update_first_row(matrix[0],1)
    for i in range(1,stringRows):
        currentRow = matrix[i]
        lastCell = 0
        cells = len(currentRow)
        for j in range(cells):
            if currentRow[j] == "0":
                if inGroup and incGroup:
                    currentGroup += 1
                    incGroup = False
                inGroup = False
                continue
            if j == 0:
#             No last cell
                currentGroup += 1
                inGroup = True
                lastRow = matrix[(i-1)]
                cellAbove = int(lastRow[j])
                if cellAbove > 0:
                    currentRow[j] = str(cellAbove)
                    incGroup = False
                    continue
                else:
                    currentRow[j] = str(currentGroup)
                    incGroup = True
                    continue
            else:
                inGroup = True
                lastRow = matrix[(i-1)]
                cellAbove = int(lastRow[j])
                lastCell = int(currentRow[j - 1])
                if cellAbove > 0:
                    if lastCell == 0:
                        currentRow[j] = str(cellAbove)
                        incGroup = False
                        continue
                    if lastCell == 1:
                        currentRow[j - 1] = str(cellAbove)
                        currentRow[j] = str(cellAbove)
                        incGroup = False
                        continue
                    if lastCell > 1:
                        prevailingGroup = min(lastCell, cellAbove)
                        lastRow[j] = str(prevailingGroup)
                        currentRow[j - 1] = str(prevailingGroup)
                        currentRow[j] = str(prevailingGroup)
                        incGroup = False
                        continue
                elif lastCell > 0:
                    if lastCell == 1:
                        prevailingGroup = currentGroup
                        currentRow[j - 1] = str(prevailingGroup)
                        currentRow[j] = str(prevailingGroup)
                        incGroup = True
                        continue
                    else:
                        currentRow[j] = str(lastCell)
                        incGroup = False
                        continue
                elif currentRow[j] == 1:
                    currentRow[j] = str(currentGroup)
                    incGroup = True
        incGroup = True
    return currentGroup

def total_used_cells(baseKey):
    grandTotal = 0
    stringRows = []
    arrayRows = []
    for i in range(128):
        rowHash = baseKey + str(i)
#         rowInDec = asciiToDecimal(rowHash)
        knotHash = hash_checker(rowHash)
        hashInBin,hashArray = hex_to_bin(knotHash)
        row = ""
        arrRow = []
        for i in hashInBin:
            row = row + str(i)
            arrRow.append(str(i))
            grandTotal += int(i)
        stringRows.append(row)
        arrayRows.append(arrRow)
    return grandTotal, stringRows, arrayRows

if __name__ == '__main__':
        
    baseString = "flqrgnkx-"
    realBase = "wenycdww-"
    
    grandTotal, stringRows, arrayRows = total_used_cells(realBase)
    
    numGroups = convert_to_groups(arrayRows)
        
    for i in stringRows:
        print(str(i))
        
    for i in arrayRows:
        print(str(i))    
        
    print("GrandTotal: " + str(grandTotal))
    print("Total Groups: " + str(numGroups))
    pass