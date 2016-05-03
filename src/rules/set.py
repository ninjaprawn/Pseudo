#!/usr/bin/python

import re

def checkIfSetFormat(line, lineCount):
    tokens = []
    settingMatch = re.compile('set (.+?) to ("?.+"?)', re.IGNORECASE)
    match = settingMatch.match(line)
    if match:
        keywords = ['set', 'to', 'if', 'is', 'equals']

        variableMatch = re.compile('^[a-z0-9]+$', re.IGNORECASE)

        if not variableMatch.match(match.group(1)):
            raise NameError('Line ' + str(lineCount) + ': \'' + line.rstrip() + '\'\n' + (
            " " * (23 + (len(str(lineCount))))) + '^\nPlease use alphanumeric variable names')
        elif match.group(1) in keywords:
            raise NameError('Line ' + str(lineCount) + ': \'' + line.rstrip() + '\'\n' + (
            " " * (23 + (len(str(lineCount))))) + '^\nPlease don\'t use reserved keywords for variable names')

        tokens.append({"type": "operator", "value": "set"})
        tokens.append({"type": "variable", "value": match.group(1)})
        tokens.append({"type": "suboperator", "value": "to"})

        intMatch = re.compile('^\d+$')
        floatMatch = re.compile('^\d+\.\d+$')

        if match.group(2).startswith('"') and match.group(2).endswith('"'):

            tokens.append({"type": "string", "value": match.group(2)[1:-1]})
        elif floatMatch.match(match.group(2)):
            tokens.append({"type": "float", "value": match.group(2)})
        elif intMatch.match(match.group(2)):
            tokens.append({"type": "integer", "value": match.group(2)})
        else:
            tokens.append({"type": "string", "value": match.group(2)})

    else:
        raise SyntaxError('Line ' + str(lineCount) + ': \'' + line.rstrip() + '\'')
    return tokens