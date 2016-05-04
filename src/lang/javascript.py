#!/usr/bin/python

def generateSet(instruction, indentationLevel):
    finalLine = "   "*indentationLevel
    finalLine += "var "
    finalLine += instruction['body']['name']
    finalLine += " = "

    finalLine += instruction['body']['value']

    finalLine += ";\n"
    return finalLine


def generateSet(name, value, type, indentationLevel):
    finalLine = "   "*indentationLevel
    finalLine += "var "
    finalLine += name
    finalLine += " = "

    if type == 'string':
        # Whatever you use for defining strings (either single, double, etc.)
        finalLine += '"' + value + '"'
    else:
        finalLine += value

    finalLine += ";\n"
    return finalLine