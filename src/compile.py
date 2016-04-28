#!/usr/bin/python

import re

fileToParse = open("../examples/0.1.pseudo")

def getToken(file):
    tokens = []
    letterMatch = re.compile('[a-z]', re.IGNORECASE)
    for line in file:
        count = 0
        while count < len(line):
            char = line[count]
            if letterMatch.match(char):
                val = ""

                while letterMatch.match(char):
                    val += char
                    count += 1
                    char = line[count]

                if val.lower() == "set":
                    tokens.append({'type': 'operator', 'value': 'set'})
                    spaceCount = 0
                elif val.lower() == "to":
                    tokens.append({'type': 'suboperator', 'value': 'to'})
                else:
                    tokens.append({'type': 'text', 'value': val})
                continue
            count += 1
        break
    return tokens

print(getToken(fileToParse))

def addOne(num):
    num += 1

x = 0
addOne(x)
print(x)

#letterMatch = re.compile('[a-z]', re.IGNORECASE)

#print letterMatch.match("0")

fileToParse.close()