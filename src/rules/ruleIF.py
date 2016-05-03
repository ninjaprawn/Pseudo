#!/usr/bin/python

import re

def checkIfIFFormat(line, lineCount):
    tokens = []
    ifMatch = re.compile('if ("?.+"?) (is|equals|is equal to) ("?.+"?)', re.IGNORECASE)
    match = ifMatch.match(line)
    if match:

        leftHandSide = match.group(1)
        rightHandSide = match.group(3)
        leftHandSideToken = None
        rightHandSideToken = None

        intMatch = re.compile('^\d+$')
        floatMatch = re.compile('^\d+\.\d+$')

        if leftHandSide.startswith('"') and leftHandSide.endswith('"'):
            leftHandSideToken = {"type": "string", "value": leftHandSide[1:-1]}
        elif floatMatch.match(leftHandSide):
            leftHandSideToken = {"type": "float", "value": leftHandSide}
        elif intMatch.match(leftHandSide):
            leftHandSideToken = {"type": "integer", "value": leftHandSide}
        else:
            leftHandSideToken = {"type": "variable", "value": leftHandSide}

        if rightHandSide.startswith('"') and rightHandSide.endswith('"'):
            rightHandSideToken = {"type": "string", "value": rightHandSide[1:-1]}
        elif floatMatch.match(rightHandSide):
            rightHandSideToken = {"type": "float", "value": rightHandSide}
        elif intMatch.match(rightHandSide):
            rightHandSideToken = {"type": "integer", "value": rightHandSide}
        else:
            rightHandSideToken = {"type": "variable", "value": rightHandSide}

        tokens.append({"type": "operator", "value": "if"})
        tokens.append(leftHandSideToken)
        tokens.append({"type": "suboperator", "value": "equals"})
        tokens.append(rightHandSideToken)
    else:
        raise SyntaxError('Line ' + str(lineCount) + ': \'' + line.rstrip() + '\'')
    return tokens