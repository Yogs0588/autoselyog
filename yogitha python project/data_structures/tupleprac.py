'''
Created on Apr 12, 2025

@author: yogs0
'''
'''Tuple: Is a data structure represented by ()
1. Creation of tuple
    - Empty list can be created
    - List with elements:
        > Manually adding elements
        > Using in-built function called tuple()
2. tuple is heterogeneous
3. Accessing elements
4. tuple cannot be modified
5. tuple stores None as a value
6. tuple stores duplicate values

'''
#1. Creation of tuple
# a. Creation of empty tuple
a = ()
print(type(a))

# b. Creation of tuple with elements
b=(1, 2, 3, 4, 5) # homogenous data structure
print(type(b))


c=(1, "abc", 4.76, True, 3+8j) # heterogeneous data structure
print(c)

# Accessing the elements using Index
print(c[4])
print(c[-1])

# Modification/ replacement using index canot be modified
#c[1]="anu" # re-initialization
#print(c)

# tuple stores None as a value
# tuple stores duplicate values

e=("Bhavani", "Chitra", "Sandeep", "Sanjana", "Vivek", "Yogitha", None, "Bhavani")
print(e)

# Insertion order is preserved
# The size of a list is not fixed or constant


e.count(c)
print(e)

# Accessing using loops
print('e-->', e)
# for loop:
print("===For loop===")
for ele in e:
    print(ele)
    
'''print('===While loop===')

i=0
while i<len(e):
    print(e[i])
    i+=1'''
    
    
    

