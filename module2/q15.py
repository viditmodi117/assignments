#Write a Python program to add 'ing' at the end of a given string (lengthshould be at least 3). If the given string already ends with 'ing' then add'ly' instead if the string length of the given string is less than 3, leave itunchanged.

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
