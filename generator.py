import random
chars = [chr(char) for char in range(ord('a'), ord('z')+1)] +  [chr(char) for char in range(ord('0'), ord('9')+1)]
chars += ['U', ' ', 'E','(',')','+','*','?']

def generate(num):
    string = ''
    for i in range(num):
        string += random.choice(chars)
    return string

for i in range(1000):
    print(generate(10))