import random

def getAnswer(answerNumber):
    if answerNumber==1:
        return'Je to jisté'
    elif answerNumber==2:
        return'Nejspíš ano'
    elif answerNumber==3:
        return'Pravděpodobně'
    elif answerNumber==4:
        return'Nejsem si jistý. Zeptej se znovu.'
    elif answerNumber==5:
        return'Není to příliš pravděpodobné'
    elif answerNumber==6:
        return'Má odpověď zní ne'

r = random.randint(1,6)
fortune = getAnswer(r)
print(fortune)
