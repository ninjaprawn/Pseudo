#!/usr/bin/python

def generateSet(instruction, indentationLevel):
    finalLine = "   "*indentationLevel
    finalLine += "instruction "
    finalLine += instruction['body']['name']
    finalLine += " assignOperator "

    if instruction['body']['type'] == 'string':
        # Whatever you use for defining strings (either single, double, etc.)
        finalLine += '"' + instruction['body']['value'] + '"'
    else:
        finalLine += instruction['body']['value']

    finalLine += "\n"
    return finalLine