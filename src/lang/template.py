#!/usr/bin/python

def generateSet(name, value, type, indentationLevel):
    finalLine = "   "*indentationLevel
    finalLine += "instruction "
    finalLine += name
    finalLine += " assignOperator "

    if value['type'] == 'string':
        # Whatever you use for defining strings (either single, double, etc.)
        finalLine += '"' + value['value'] + '"'
    else:
        finalLine += value['value']

    finalLine += "\n"
    return finalLine