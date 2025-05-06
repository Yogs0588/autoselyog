'''
Created on Apr 12, 2025

@author: yogs0
'''

d1={}
print(type(d1))

students_list={1:'Anu', 2:'Bhavani', 3:'Chira',4:'Deepak',5:'Nayu',6:'Sanjana',7:'Zavi'}
print(students_list)


#buildin function 
#students_list= dict(1='arya')
#print(students_list)


#place holder dict
d3=dict.fromkeys([1,2,3,4], 'abc')
print(d3)


d2={1:'one', 2:'two'}
print(d2)

# check for duplicates- does not allow duplicates element
print('---duplicate value----')
students_list2={1:'Anu', 2:'Bhavani', 3:'Deepak',4:'Deepak'}
print(students_list2)

# check for duplicates- does not allow duplicates key but allow duplicate value
students_list2={1:'Anu', 2:'Bhavani', 3:'Deepak',3:'yogs'}
print(students_list2)

students_list2={1:'Anu', 2:'Bhavani', 3:'Deepak',4:'Deepak'}
print(students_list2)

# to get  value from dict
print('---access----')
stdlt={1:'Anu', 2:'Bhavani', 3:'Chira',4:'Deepak',5:'Nayu',6:'Sanjana',7:'Zavi'}
print(stdlt[2])

students_list4={'Anu':1, 'Bhavani':2, 'Deepak':3}
print(students_list4['Anu'])




# to get keys and values seperately
print('---keys or values----')
print(stdlt.keys())

print(stdlt.values())

# to itrate values and key
print('---values----')
for n in stdlt.values():
    print(n)


for n in stdlt.keys():
    print(n)


# modify/replace

print('---modify---')
stdlt1={1:'Anu', 2:'Bhavani', 3:'Chira',4:'Deepak',5:'Nayu',6:'Sanjana',7:'Zavi'}

stdlt1[3]='chand' #replace
print(stdlt1)


stdlt1[8]='Yogs' #insertion
print(stdlt1)

# functions

f=stdlt1.copy() #copy
print(f)


print(f.items()) # to get the item


print(f.pop(1)) # to remove a key item 
print(f)

print(f.popitem()) # to remove last item
print(f)

print(f.setdefault(4))
print(f)

f.update(d2) # update the dictionary with other dict
print(f)

# city and pincode
pincity= {'agra':570010,'bangalore':570011,'Delhi':570012,'finland':570013, 'London':570014,'mysore':570015}






