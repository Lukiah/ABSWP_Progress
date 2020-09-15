def spam():
    global eggs
    eggs = 'spam' #toto je v global

def bacon():
    eggs = 'bacon' #toto je v local

def ham():
    print(eggs) #toto "eggs" je global

eggs = 42 #toto je global
spam()
print(eggs)