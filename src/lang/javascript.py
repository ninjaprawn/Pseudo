#!/usr/bin/python

def generateSet(instruction, indentationLevel):
    finalLine = "   "*indentationLevel
    finalLine += "var "
    finalLine += instruction['body']['name']
    finalLine += " = "

    finalLine += instruction['body']['value']

    finalLine += ";\n"
    return finalLine