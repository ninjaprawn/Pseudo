#!/usr/bin/python

import re

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
                    settingMatch = re.compile('set (.+?) to ("?.+"?)', re.IGNORECASE)
                    match = settingMatch.match(line)
                    if match:
                        keywords = ['set', 'to', 'if', 'is', 'equals']

                        variableMatch = re.compile('^[a-z0-9]+$', re.IGNORECASE)

                        if not variableMatch.match(match.group(1)):
                            raise NameError('Line ' + str(lineCount) + ': \'' + line.rstrip() + '\'\n'+(" "*(23+(len(str(lineCount)))))+'^\nPlease use alphanumeric variable names')
                        elif match.group(1) in keywords:
                            raise NameError('Line ' + str(lineCount) + ': \'' + line.rstrip() + '\'\n'+(" "*(23+(len(str(lineCount)))))+'^\nPlease don\'t use reserved keywords for variable names')

                        tokens.append({"type": "operator", "value": "set"})
                        tokens.append({"type": "variable", "value": match.group(1)})
                        tokens.append({"type": "suboperator", "value": "to"})

                        intMatch = re.compile('^\d+$')
                        floatMatch = re.compile('^\d+\.\d+$')

                        if match.group(2).startswith('"') and match.group(2).endswith('"'):
                            tokens.append({"type": "string", "value": match.group(2)})
                        elif floatMatch.match(match.group(2)):
                            tokens.append({"type": "float", "value": match.group(2)})
                        elif intMatch.match(match.group(2)):
                            tokens.append({"type": "integer", "value": match.group(2)})
                        else:
                            tokens.append({"type": "string", "value": match.group(2)})

                    else:
                        raise SyntaxError('Line ' + str(lineCount) + ': \'' + line.rstrip() + '\'')

                continue
            count += 1
        lineCount += 1
    return tokens

print(getTokens(fileToParse))

fileToParse.close()