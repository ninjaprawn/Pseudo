#!/usr/bin/python

import re
from rules import ruleIF, ruleSET

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
            elif currentSequence['name'] == 'if':
                count += 1
                leftHandSide = tokens[count]
                count += 1
                comparingType = tokens[count]
                count += 1
                rightHandSide = tokens[count]

                currentSequence['body'] = {'left': leftHandSide, 'right':  rightHandSide, 'comparing type': comparingType['value']}
            elif currentSequence['name'] == 'fi':
                count += 1
                currentSequence['name'] = 'endif'

            ast.append(currentSequence)
            continue

        count += 1
    return ast

# Swift For Now
def generateCode(ast):
    finalCode = ""
    indentation = ""
    for instruction in ast:
        if instruction['type'] == 'operation':
            if instruction['name'] == 'set':
                finalCode += indentation
                finalCode += "let "
                finalCode += instruction['body']['name']
                finalCode += " = "
                if instruction['body']['type'] == 'string':
                    finalCode += '"' + instruction['body']['value'] + '"'
                else:
                    finalCode += instruction['body']['value']
                finalCode += "\n"
            elif instruction['name'] == 'if':
                finalCode += indentation
                indentation += "    "
                finalCode += "\nif "
                if instruction['body']['left']['type'] == "string":
                    finalCode += '"' + instruction['body']['left']['value'] +'"'
                else:
                    finalCode += instruction['body']['left']['value']

                finalCode += " == "
                if instruction['body']['right']['type'] == "string":
                    finalCode += '"' + instruction['body']['right']['value'] +'"'
                else:
                    finalCode += instruction['body']['right']['value']
                finalCode += " {\n\n"

            elif instruction['name'] == 'endif':
                if len(indentation) > 0:
                    indentation = indentation[:-4]
                finalCode += indentation
                finalCode += "\n}\n"

    return finalCode

tokens = getTokens(fileToParse)

fileToParse.close()

ast = transformer(tokens)

#print(ast)

print(generateCode(ast))