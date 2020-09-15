# Toto není nejlepší demonstrace random.choice(list), ale funguje to, jak má
import random
print('Hi, I will randomly choose a pet for you')
pets = ['Dog','Cat','Fish','Mice','Songbirds']
while True:
    print('Do you like ' + random.choice(pets) + '? (Yes/No)')
    answer = input()
    if answer == 'No':
        continue
    elif answer == 'Yes':
        break

print('Enjoy your new pet')



