'''
Created on Apr 15, 2025

@author: yogs0
'''
'''Strings: word/ phrase/ sentence/ paragraph

letters: Characters in python

Def: String is a character/ collection of characters

'''

name = "yogs"

print("name:", name)
print(type(name))

#Empty string
nick_name=''
print("nick_name:",nick_name)
print(type(nick_name))

age="34" # 34 is considered as a string
print("age:", age)
print(type(age))

#Access using Index
print(name[0])

#Access using for loop
print("===Access using for loop===")
for letter in name:
    print(letter)
 
#Access using slicing operator
print("===Access using slicing operator===")
print(name[1:4])  
print(type(name[1:4])) 

address="""iQuest,

Hebbal Industrial area,

Mysuru.
"""
print(address)

#Modification: String is immutable/ String can't be modified
# name[0]="z" #TypeError: 'str' object does not support item assignment


modified_name=name.replace('N', 'I')
print("name:",name)
print("modified_name:", modified_name)

# CAPITALIZE AND STRIP(removes the whitespace)

print("capitalize first char:", name.capitalize()) # it will not capitalize since it has space
print(name.strip().capitalize())

print(address.casefold()) # to convert in lowercase

print(name.count('v')) # counts how many time it is there

print(name.upper()) # to convert in uppercase

print(name.find('g')) # to find the position/ index

print(name.index('s')) # to find the position/ index

print(name.isalnum()) # to find whether it conntains  alpha number

print(name.isalpha()) 

