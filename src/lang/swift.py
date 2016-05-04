#!/usr/bin/python

def generateSet(instruction, indentationLevel):
    finalLine = "   "*indentationLevel
    finalLine += "let "
    finalLine += instruction['body']['name']
    finalLine += " = "

    if instruction['body']['type'] == 'string':
        finalLine += '"' + instruction['body']['value'] + '"'
    else:
        finalLine += instruction['body']['value']

    finalLine += "\n"
    return finalLine


def generateSet(name, value, type, indentationLevel):
    finalLine = "   "*indentationLevel
    finalLine += "let "
    finalLine += name
    finalLine += " = "

    if type == 'string':
        # Whatever you use for defining strings (either single, double, etc.)
        finalLine += '"' + value + '"'
    else:
        finalLine += value

    finalLine += "\n"
    return finalLine