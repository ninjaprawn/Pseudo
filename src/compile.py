#!/usr/bin/python

import re
from rules import *

fileToParse = open("../examples/0.1.pseudo")

def getTokens(file):
    tokens = []
    letterMatch = re.compile('[a-z]', re.IGNORECASE)
    lineCount = 1
    for line in file:
        count = 0
        if line.startswith("//"):
            # Ignores single line comments, like normal compilers
            continue

        while count < len(line):
            char = line[count]
            if letterMatch.match(char):
                val = ""

                while letterMatch.match(char):
                    val += char
                    count += 1
                    char = line[count]

                if val.lower() == "set":
                    newTokens = set.checkIfSetFormat(line, lineCount)
                    tokens.extend(newTokens)

                continue
            count += 1
        lineCount += 1
    return tokens


def transformer(tokens):
    ast = []
    count = 0
    while count < len(tokens):
        token = tokens[count]
        if token['type'] == 'operator':
            currentSequence = {'type': 'operation', 'name': token['value'], 'body': []}
            if currentSequence['name'] == 'set':
                count += 1
                variableName = tokens[count]
                count += 2
                variableContents = tokens[count]

                currentSequence['body'] = {'name': variableName['value'], 'value':variableContents['value'], 'type':variableContents['type']}
            ast.append(currentSequence)
            continue

        count += 1
    return ast

# Swift For Now
def generateCode(ast):
    finalCode = ""
    for instruction in ast:
        if instruction['type'] == 'operation':
            if instruction['name'] == 'set':
                finalCode += "let "
                finalCode += instruction['body']['name']
                finalCode += " = "
                if instruction['body']['type'] == 'string':
                    finalCode += '"' + instruction['body']['value'] + '"'
                else:
                    finalCode += instruction['body']['value']
                finalCode += "\n"
    return finalCode

tokens = getTokens(fileToParse)

fileToParse.close()

ast = transformer(tokens)

print(generateCode(ast))