#!/usr/bin/python

import re

fileToParse = open("../examples/0.1.pseudo")

def getTokens(file):
    tokens = []
    letterMatch = re.compile('[a-z]', re.IGNORECASE)
    lineCount = 0
    for line in file:
        count = 0
        print(line.strip())
        while count < len(line):
            char = line[count]
            if letterMatch.match(char):
                val = ""

                while letterMatch.match(char):
                    val += char
                    count += 1
                    char = line[count]

                if val.lower() == "set":
                    settingMatch = re.compile('set .+? to "?.+?"?', re.IGNORECASE)
                    if settingMatch.match(line):
                        print("Passed")
                    else:
                        raise Exception('Syntax error on line ' + str(lineCount) + ': ')

                continue
            count += 1
        #break
        lineCount += 1
    return tokens

print(getTokens(fileToParse))

fileToParse.close()