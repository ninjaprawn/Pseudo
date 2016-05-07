#!/usr/bin/python

def generateSet(name, value, type, indentationLevel):
    finalLine = "    "*indentationLevel
    finalLine += name
    finalLine += " = "

    if type == 'string':
        # Whatever you use for defining strings (either single, double, etc.)
        finalLine += '"' + value + '"'
    else:
        finalLine += value

    finalLine += "\n"
    return finalLine


def generateIf(comparison, leftHandType, leftHandValue, rightHandType, rightHandValue, indentationLevel):
    finalLine = "    " * indentationLevel
    finalLine += "if "
    if leftHandType == "string":
        finalLine += '"' + leftHandValue + '"'
    else:
        finalLine += leftHandValue

    if comparison == "equals":
        finalLine += " == "

    if rightHandType == "string":
        finalLine += '"' + rightHandValue + '"'
    else:
        finalLine += rightHandValue

    finalLine += ":\n"
    return finalLine

def generateEndIf(indentationLevel):
    finalLine = "    "*indentationLevel
    finalLine += "\n"
    return finalLine