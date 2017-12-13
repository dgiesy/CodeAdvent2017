'''
Created on Dec 13, 2017

@author: dgiesy
'''

def read_data(fileName):
    with open(fileName) as junk:
        walls = {}
        content = junk.readlines()
        for line in content:
            cleanContent = line.split(": ")
            walls[cleanContent[0]]=cleanContent[1].strip()
    return walls


if __name__ == '__main__':
    fileName = "../compressedFirewalls.txt"
    
    compressedFirewalls = read_data(fileName)
#     Create a disposable copy
    fw2 = dict(compressedFirewalls)
    
    while len(fw2) > 0:
        break
    
    
    pass
