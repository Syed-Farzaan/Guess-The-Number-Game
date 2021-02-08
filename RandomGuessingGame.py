# import pyjokes
# joke = pyjokes.get_joke('en', 'neutral')
# print(joke)

from random import randint
answer = randint(1, 10)

print('Salaam to you user, Welcome to our new game')
print('In this game you have to guess a number')

while True:
    try:
        guess = int(input("Guess the number between 1-10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("Oh Boy, You Are A Genius!")
                break
        else:
            print("Hey Stupid, I said between 1-10")
    except ValueError:
        print('Enter a number please.... ')
