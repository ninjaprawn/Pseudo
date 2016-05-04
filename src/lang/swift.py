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