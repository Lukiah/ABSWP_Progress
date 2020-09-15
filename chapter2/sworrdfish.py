while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hi Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        print('ACCESS GRANTED')
        break
