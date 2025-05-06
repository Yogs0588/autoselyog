'''
Created on Apr 6, 2025

@author: yogs0
'''
# Creation of list
#a. creation of empty list
a={}
print(type(a))

# b.creation of  list with elements
a=[1,32/3,2.36,'adfg',True]
print(type(a))

# DEFINING DICTIONARY
C={1:'YOGS'}
print(type(C))

# CREATION ELEMENT
d=list(range(20))
print(d)

#Accessing elements using index
print(a[3])
print(a[-2])

# modification or replace using index
# modification or replace can be only with list not with Tuple or set
a[1]='yogs'
print(a)


# slicing operator
print('d[::}',d[::])
print('d[3:9}',d[3:9])
print('d[:9}',d[:9])
print('d[3:}',d[3:])
print('d[3:9:3}',d[3:9:3])
print('d[-12:-9:3}',d[-12:-9:3])
print('d[::3}',d[::3])
print('d[::-1}',d[::-1])
print('d[-12:-9:-1}',d[-12:-9:-1])

print('----for loop-----')
for ele in a:
    print(ele)


print('----while loop-----')
i=0
while i<5:
    print(a[i])
    i+=1
    
    
#finding length of collection
print(len(a))
  
# print odd number from the list(d)
    
''' if n%2 == 1:
        print(n)'''

# finding word using a letter

e=["Bhavani", "Chitra", 'aniv',"Sandeep", "Sanjana", "Vivek", "Yogitha",'aniv']

for g in e:
    if 'a' in g:
        print(g)
        
        
# to add a object in last 

e.append('ANIV')
print(e)

# to replace object from list
e.insert(4, 'pooja')
print(e)

# to find count
print(e.count('aniv'))

#
e.extend(a)
print(e.extend(a),e)

print(e.index('aniv'))


print('count',e.count('aniv'))
print('index',e.index('aniv'))


print(a)
print(a.remove(True))
print(a)
print(a.pop(3))
print(a)












