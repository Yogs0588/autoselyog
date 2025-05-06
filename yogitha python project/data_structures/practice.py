'''
Created on Apr 7, 2025

@author: yogs0
'''
print('------fizzBuzz problem-----------')

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')   
    else:
        print(n)
        
print('------reverse a string-----------')
a='hello'
print('hello: ',a[-1:-6:-1])

print('---------non repeating char-----')

b = 'aabbccde'
for i in b:
    if(b.count(i) == 1):
        print(i)
        
        
print('---------count of frequency----')
        
word =input('type a word ')
# create dictionary to store key value pair
dict = {}

for j in word:
    # if j already appears as key in dict, increment the count
    if j in dict:
        dict[j] += 1

    # else j appears for the first time, add to dict
    else:
        dict[j] = 1

# printing result 
print(dict)


# list of squares for odd numbers
e=[]
d=[15,30,22,10,60,13]

for n in d:
    if n%2 == 1:
        #print(n**2)
        e.append(n**2)
print(e)  
           
         
    

















                
    