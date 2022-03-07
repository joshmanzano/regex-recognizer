import csv
import json
import tokenizer

global stack 
global table 
global tokenList
global verbose
verbose = False
# hi nike hallo
def loadParsingTable(filename):
    global table
    with open(filename, 'r') as f:
        line = f.read()
        table = json.loads(line)

def readInput(filename):
    inputLines = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            inputLines.append(line)
    return inputLines

def lexicalAnalysis(string):
    tokens = tokenizer.tokenize(string)
    valid = True
    if(verbose):
        print('String:',string)
    if('invalid' in tokens):
        if(verbose):
            print('Lexical error')
        valid = False
    else:
        if(verbose):
            print('Tokens:',tokens)

    return tokens, valid

def syntaxAnalysis(tokens):
    stack = ['$']
    stack.append('S')
    for t in tokens:
        rule = stack.pop()
        while(t != rule):
            # print(rule, stack)
            try:
                newRules = table[rule][t]
            except KeyError:
                return t, False
            # print('New rules:',newRules)
            for r in newRules:
                stack.append(r)
            # print(rule, stack)
            rule = stack.pop()
            # print(rule, stack)
            # print(t, '==' ,rule)
    # print('End stack:',stack)
    return t, True

def process(input_file , output_file):
    output = []
    inputLines = readInput(input_file) 
    for line in inputLines:
        line = line.strip()
        tokens, validLex = lexicalAnalysis(line)
        if(validLex):
            rule, validSyn = syntaxAnalysis(tokens)
            if(validSyn):
                if(verbose):
                    print('Syntax:','ACCEPT')
                else:
                    result = line + ' - ' + 'ACCEPT'
                    print(result)
                    output.append(result)
            else:
                if(verbose):
                    print('Syntax:','REJECT') 
                else:
                    result = line + ' - ' + 'REJECT'
                    print(result)
                    output.append(result)
        else:
            result = line + ' - ' + 'REJECT'
            print(result)
            output.append(result)
        if(verbose):
            print('===')
    return output

input_file = input('Enter input filename: ')
output_file = input('Enter output filename: ')
loadParsingTable('table.json')
output = process(input_file, output_file)

with open(output_file, 'w') as f:
  for result in output:
    f.write(result+'\n')


