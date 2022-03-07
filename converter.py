import csv
import json
import tokenizer

def readInput(filename):
    inputLines = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            inputLines.append(line)
    return inputLines

def lexicalAnalysis(string):
    tokens = tokenizer.tokenize(string)
    if('invalid' in tokens):
        return None
    else:
        return tokens

def process(filename):
    inputLines = readInput(filename) 
    for line in inputLines:
        line = line.strip()
        tokens = lexicalAnalysis(line)
        if tokens != None:
            new = ''
            for t in tokens:
                if t == 'char':
                    new += 'c'
                elif t == 'union':
                    new += 'u'
                elif t == 'symbol':
                    new += 's'
                elif t == 'epsilon':
                    new += 'e'
                elif t == '(':
                    new += '('
                elif t == ')':
                    new += ')'
                else:
                    pass
            print(new)

input_file = input('Enter input filename: ')
process(input_file)