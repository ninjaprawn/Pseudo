#!/usr/bin/python

def generateSet(name, value, type, indentationLevel):
    finalLine = "    "*indentationLevel
    finalLine += "instruction "
    finalLine += name
    finalLine += " assignOperator "

    if type == 'string':
        # Whatever you use for defining strings (either single, double, etc.)
        finalLine += '"' + value + '"'
    else:
        finalLine += value

    finalLine += "\n"
    return finalLine


def generateIf(comparison, leftHandType, leftHandValue, rightHandType, rightHandValue, indentationLevel):
    finalLine = "    " * indentationLevel
    finalLine += "instruction "
    if leftHandType == "string":
        finalLine += '"' + leftHandValue + '"'
    else:
        finalLine += leftHandValue

    if comparison == "equals":
        finalLine += " equalsOperator "

    if rightHandType == "string":
        finalLine += '"' + rightHandValue + '"'
    else:
        finalLine += rightHandValue

    finalLine += " startIfBody"
    return finalLine

def generateEndIf(indentationLevel):
    finalLine = "    "*indentationLevel
    finalLine += "endIfBody"
    return finalLine