# write a program to check type of characters enterd by user
char = input('Enter a character to check type of characters ')

if char.isalnum():
    if char.isdigit():
     print("it is a digit")
    else:
       print('it is a alphabate')
       if char.isupper():
          print('it is a uppercase character')
       else :
          print('it is a lowercase character')
elif char.isspace:
   print('it is space')
else:
   print('it is a symbol')
