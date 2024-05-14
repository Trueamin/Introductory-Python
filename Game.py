import random
Answer = random.randint(1, 999)

Name = input('Whats is your name? ')
Guess = int(input('What is yor guess? '))

while Guess != Answer:
    if Guess > Answer:
        print('mine is smaller!')
    else:
        print('mine is larger!')
    Guess = int(input('What is yor guess? '))

print('woooowwww!!!', Name, 'Name you did it! you rock!')
