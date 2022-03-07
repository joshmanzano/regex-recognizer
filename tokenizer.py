import json

class Tokenizer:
    def __init__(self, states):
        self.states = states
        self.current = 0

    def process(self, string, index, startState):
        self.currentState = self.states[startState]
        while(True):
            if(index < len(string)):
                character = string[index]
                if(self.currentState.hasTransition(character)):
                    toState = self.currentState.transition(string[index])
                    index += 1
                    self.currentState = self.states[toState]
                else:
                    return self.currentState.name, index
            else:
                return self.currentState.name, index
        
class State:
    def __init__(self, name, stateNumber):
        self.stateNumber = stateNumber
        self.name = name 
        self.transitions = {}

    def addTransition(self, character, stateNumber):
        self.transitions[character] = stateNumber

    def transition(self, character):
        return self.transitions[character]

    def hasTransition(self, character):
        return character in self.transitions

global program
global states

with open('states.json', 'r') as f:
    global states
    states = {}
    data = json.loads(f.read())
    for stateData in data['states']:
        state = State(stateData['name'],int(stateData['stateNumber']))
        for transition in stateData['transitions']:
            try:
                state.addTransition(transition['character'], int(transition['stateNumber']))
            except:
                state.addTransition(transition['character'], transition['stateNumber'])
        states[int(stateData['stateNumber'])] = state

tokenizer = Tokenizer(states)

def getNextToken(string, index):
    return tokenizer.process(string, index, 0)

def tokenize(string):
    tokens = []
    index = 0
    invalid = False
    while(index < len(string) and not invalid):
        token, index = getNextToken(string, index)
        if(token != 'invalid'):
            tokens.append(token)
        else:
            tokens = ['invalid']
            invalid = True
    tokens.append('$')

    return tokens