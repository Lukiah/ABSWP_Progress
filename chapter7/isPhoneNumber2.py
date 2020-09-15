import re
def isphonenumber():
    text = input()
    phoneNumberRegex = re.compile(r'(\+\d\d\d\d\d\d\d\d\d\d\d\d)')
    mo = phoneNumberRegex.search(text)
    if mo == "":
        print('Nenalezli jsme žádné telefonní číslo v textu')
    else:
        print(mo.group())

isphonenumber()