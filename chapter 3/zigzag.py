import time, sys
indent = 0 #kolik odsadit
indentIncreasing = True

try:
    while True: #main loop
        print(' '*indent, end='')
        print('0000000000')
        time.sleep(0.2) #pauza na 1/5 sekundy

        if indentIncreasing:
            #Zvyšuje odsazení
            indent = indent + 1 # velikost odsazení dopředu
            if indent == 20: # velikost odsazení, při kterém program změní směr
                # Change direction:
                indentIncreasing = False

        else:
            #snižuje odsazení
            indent = indent - 1 #velikost odsazení zpět (1 mezera zpět)
            if indent == 0: #velikost odsazení, při kterém program změní směr
                #změna směru
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()