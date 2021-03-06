#!/usr/bin/python

import re
from rules import *
from lang import *

fileToParse = open("../examples/0.2.pseudo")

def getTokens(file):
    tokens = []
    letterMatch = re.compile('[a-z]', re.IGNORECASE)
    lineCount = 1
    for line in file:
        line = line.strip()
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
                    if count >= len(line):
                        break
                    else:
                        char = line[count]

                if val.lower() == "set":
                    newTokens = ruleSET.checkIfSetFormat(line, lineCount)
                    tokens.extend(newTokens)
                elif val.lower() == "if":
                    newTokens = ruleIF.checkIfIFFormat(line, lineCount)
                    tokens.extend(newTokens)
                elif val.lower() == "fi":
                    tokens.append({"type": "operator", "value": "fi"})

                break
            count += 1
        lineCount += 1
    return tokens


def transformer(tokens):
    ast = []
    count = 0
    variables = {}
    while count < len(tokens):
        token = tokens[count]
        if token['type'] == 'operator':
            currentSequence = {'type': 'operation', 'name': token['value'], 'body': []}
            if currentSequence['name'] == 'set':
                count += 1
                variableName = tokens[count]

                count += 2
                variableContents = tokens[count]

                variables[variableName['value']] = variableContents['type']

                currentSequence['body'] = {'name': variableName['value'], 'value':variableContents['value'], 'type':variableContents['type']}
            elif currentSequence['name'] == 'if':
                count += 1
                leftHandSide = tokens[count]
                count += 1
                comparingType = tokens[count]
                count += 1
                rightHandSide = tokens[count]

                if leftHandSide['type'] == 'variable':
                    if leftHandSide['value'] not in variables.keys():
                        raise ReferenceError('Variable named ' + leftHandSide['value'] + ' has not been created.')

                if rightHandSide['type'] == 'variable':
                    if rightHandSide['value'] not in variables.keys():
                        raise ReferenceError('Variable named ' + rightHandSide['value'] + ' has not been created.')

                leftType = leftHandSide['type']
                rightType = rightHandSide['type']

                if leftType == 'variable':
                    leftType = variables[leftHandSide['value']]

                if rightType == 'variable':
                    rightType = variables[rightHandSide['value']]

                if leftType != rightType:
                    raise TypeError('Cannot compare type ' + leftType + ' with type ' + rightType)

                currentSequence['body'] = {'left': leftHandSide, 'right':  rightHandSide, 'comparing type': comparingType['value']}
            elif currentSequence['name'] == 'fi':
                count += 1
                currentSequence['name'] = 'endif'

            ast.append(currentSequence)
            continue

        count += 1
    return ast

# Swift For Now
def generateCode(ast, lang=swift):
    finalCode = ""
    indentation = 0
    for instruction in ast:
        if instruction['type'] == 'operation':
            if instruction['name'] == 'set':
                finalCode += lang.generateSet(instruction['body']['name'], instruction['body']['value'], instruction['body']['type'], indentation)
            elif instruction['name'] == 'if':
                finalCode += lang.generateIf(instruction['body']['comparing type'], instruction['body']['left']['type'], instruction['body']['left']['value'], instruction['body']['right']['type'], instruction['body']['right']['value'], indentation)
                indentation += 1
            elif instruction['name'] == 'endif':
                if indentation > 0:
                    indentation -= 1
                finalCode += lang.generateEndIf(indentation)

    return finalCode

tokens = getTokens(fileToParse)

fileToParse.close()

ast = transformer(tokens)

print(generateCode(ast, python))