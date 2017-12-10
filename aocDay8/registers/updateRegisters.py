'''
Created on Dec 9, 2017

@author: Zog
'''
import sys
import operator

class Instruction(object):
    regName = ""
    direction = ""
    amount = 0
    condReg = ""
    condOp = ""
    condValue = 0
    
    def __init__(self, regName, direction, amount, condReg, condOp, condValue):
        self.regName = regName
        self.direction = direction
        self.amount = amount
        self.condReg = condReg
        self.condOp = condOp
        self.condValue = condValue

def make_instruction(regName, parent, amount, condReg, condOp, condValue):
    instruction = Instruction(regName, parent, amount, condReg, condOp, condValue)
    return instruction

def print_instruction(inst):
    print("Register Name: " + inst.regName + ", direction: " + inst.direction + ", increment: " + str(inst.amount) + ", Condition Register Name: " + inst.condReg + ", conditional: " + inst.condOp + ", conditional value: " + str(inst.condValue))

def read_data(fileName):
    with open(fileName) as junk:
        content = junk.readlines()
    cleanContent = [x.strip() for x in content]
    return cleanContent

def format_instructions(instStrings):
    prettyInstructions = []
    for string in instStrings:
        parts = string.split()
        prettyInstructions.append(make_instruction(parts[0], parts[1], int(parts[2]), parts[4], parts[5], int(parts[6])))
    return prettyInstructions


if __name__ == '__main__':
    fileName = "../instructionSet.txt"
    ops = {"<":operator.lt, ">":operator.gt, "==":operator.eq, "!=":operator.ne, "<=":operator.le, ">=":operator.ge, "dec":operator.sub, "inc":operator.add}
    registers = {}
    allTimeHigh =  -sys.maxsize
    largestRegValue = -sys.maxsize
    rawInstructions = read_data(fileName)
    formattedInstructions = format_instructions(rawInstructions)
    
    for inst in formattedInstructions:
        if not inst.regName in registers:
            registers[inst.regName] = 0
        if not inst.condReg in registers:
            registers[inst.condReg] = 0
        if ops[inst.condOp](registers[inst.condReg], inst.condValue):
            registers[inst.regName] = ops[inst.direction](registers[inst.regName],inst.amount)
        if registers[inst.regName] > allTimeHigh:
            allTimeHigh = registers[inst.regName]
    
    for key in registers:
        if registers[key] > largestRegValue:
            largestRegValue = registers[key]
#         print("Key: " + key + "    Value: " + str(registers[key]))
    print("Largest Ending Register Value: " + str(largestRegValue))
    print("largest Register Value at any point: " + str(allTimeHigh))
    
    pass