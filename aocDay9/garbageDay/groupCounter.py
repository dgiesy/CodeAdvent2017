'''
Created on Dec 9, 2017

@author: Zog
'''


def read_data(fileName):
    fd = open(fileName,'rU')
    chars = []
    for line in fd:
        for c in line:
            chars.append(c)
    return chars



if __name__ == '__main__':
    
    garbageFile = "../charStream.txt"
#     testStrings = ["<>", "<random characters>", "<<<<>", "<{!>}>", "<!!>", "<!!!>>", "<{o\"i!a,<{i<a>"]
#     testStrings =  ["{}", "{{{}}}", "{{},{}}", "{{{},{},{{}}}}", "{<{},{},{{}}>}", "{<a>,<a>,<a>,<a>}", "{{<a>},{<a>},{<a>},{<a>}}", "{{<ab>},{<ab>},{<ab>},{<ab>}}", "{{<!!>},{<!!>},{<!!>},{<!!>}}", "{{<a!>},{<a!>},{<a!>},{<ab>}}"]
#     testStrings =  ["{{<a!>},{<a!>},{<a!>},{<ab>}}"]
    testStrings = [read_data(garbageFile)]
    for i in range(0,len(testStrings)):
        garbageStream = list(testStrings[i])
        ignoreFlag = False
        groupCounterStack = []
        garbageFlag = False
        groupGrandTotal = 0
        garbageGrandTotal = 0
        
        for currentChar in garbageStream:
            if ignoreFlag:
                ignoreFlag = False
                continue
            if currentChar == "!":
                ignoreFlag = True
                continue
            if currentChar  == "<" and not garbageFlag:
                garbageFlag = True
                continue
            if garbageFlag:
                if currentChar == ">":
                    garbageFlag = False
                    continue
                else:
                    garbageGrandTotal = garbageGrandTotal + 1
                    continue
            if currentChar == "{":
                if len(groupCounterStack) > 0:
                    groupCounterStack.append(groupCounterStack[-1] + 1)
                else:
                    groupCounterStack.append(1)
                continue
            if currentChar =="}":
                groupGrandTotal = groupGrandTotal + groupCounterStack.pop()
        
        print("Total value of all groups is: " + str(groupGrandTotal))
        print("Total non-cancelled garbage characters: " + str(garbageGrandTotal))
    
    pass