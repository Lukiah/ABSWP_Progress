catNames = [] # list
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + '(Or enter nothing and stop the list):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # spojení listu
print('The cat names are:')
for name in catNames: # loop pro výpis všech "name" v listu "catNames"
    print(' ' + name)