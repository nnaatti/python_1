from unicodedata import name


name=input('please enter your name ')
age=int (input(f'Hello {name} enter your age '))

#if condition 

if age >= 18:
    print(f'wwelcom {name} your id is: NAME-{name} AGE-{age}')

#elseif condition

elif age<18:
    print('-*-*-*-*-*-*-*-*you are not eligible-*-*-*-*-*')
