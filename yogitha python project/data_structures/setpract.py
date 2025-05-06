'''
Created on Apr 13, 2025

@author: yogs0
'''
a={2,3}     
print(a)                              #to represent the set,we can denoted set as {} flower bracket
print(type(a))                         # this is a set type

# creation of set
 
b={1, 2, 3, 4, 5}           #homogeneous data 
print(type(b))
print(b)

c={1, "abc", 4.27, True, 3+8j}   #heterogeneous data 
print(c)

#ACCESSING THE ELEMENTS USING INDEX
#print(c[4])
#print(c[-1])

#not modified for set

z={1,3,7,9,3,11}
z[3]=22
print(z)    #not modified for tuple

#modification

b.add(6)      #adding elements in set by using add keyword
print(b)

b.update([1,2,3])   #adding multiple elements by using update keyword              
print(b)

b.add("d")
print(b)

b.update("d","e","f")
print(b)

b.discard(6)     #to remove the elements from set
print(b)


