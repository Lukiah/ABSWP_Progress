#Program vyhledávající telefonní číslo a e-mail adresu
import re
text = 'My email is bojack.horseman@email.com and my phone number is +666132132132'
phoneRegex = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
emailRegex = re.compile(r'\w+\.\w+\@\w+\.\w+')
mo1 = phoneRegex.search(text)
mo2 = emailRegex.search(text)
print('Email found in text: ' + mo1.group())
print('Phone number found in text: ' + mo2.group())