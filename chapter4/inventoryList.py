inventory = []
while True:
    print('Název evidovaného zboží č.' + str(len(inventory) + 1) + ' (Pro konec evidence stiskněte enter)')
    item = input()
    if item == '':
        break
    inventory = inventory + [item]
print('The Inventory is:' + \
      '') # jen test "continuation character" (\)
for item in inventory:
    print(' ' + item)