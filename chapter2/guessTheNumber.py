#Hra využívající range() a random
import random
secretNumber = random.randint(1,20)
print('Guess a number from 1 to 20')

print('You have 6 guesses')
for guessesTaken in range(1,7):
    print('Guess the secret number')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
    else:
        break #V případě, že se hráč trefí do random čísla (secretNumber) loop se ukončí
if guess == secretNumber:
    print('Congratulations, you guessed the number on your ' + str(guessesTaken) + '. guess')
else:
    print('Too bad. You could not guess my number :c')
    print('Oh and by the way, the number was' +str(secretNumber))