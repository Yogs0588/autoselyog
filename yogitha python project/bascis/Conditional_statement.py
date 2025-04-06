'''
Created on Mar 29, 2025

@author: yogs0
'''
'''age=int(input('enter your age:'))
if age>18:
    print('Adult')
else:
    print('child')'''
    
'''age=int(input('enter your age:'))
if age<12:
    print('child')
elif age<18 and age >12:
    print('Adolescent')
elif age<=18 and age<=59:
    print('adult')
else:
    print('senior')'''
  
  
age=int(input('enter your age:'))
if age>=0:
    if age in range(0,13):
        print('child')
    elif age in range(13,19):
        print("adolescent")
    elif age in range(19,60):
        print('adult')
    else:
        print('senior')
else:
    print('please enter positive age')
  
    