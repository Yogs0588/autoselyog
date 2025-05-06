'''
Created on May 5, 2025

@author: yogs0
'''
a=2
b=5
c=a+b 
print(f"Sum of {a} and {b}:", c)

a=6
b=7
c=a+b 
print(f"Sum of {a} and {b}:", c)

# Function without parameters
def welcome():
    print("Hello people! Welcome to World!")
    print("I hope you're doing well!")

welcome()


#Function with parameters


'''def addition(a, b):
    c=a+b 
    print(f"Addition of {a} and {b}:", c)
addition(10, 20)'''

# function to return (not to print)

def addition(a, b):
    c=a+b 
    return c
d=addition(10, 20)
print(d)

def multiplication(num,multiplier):
    result_mul=num*multiplier
    print(result_mul)
    return result_mul
    
multiplication(addition(10, 20), 5) # passing a function as parameter to another function

# division
def division_integer_division(dividend, divisor):
    div_quotient = dividend/divisor
    int_div_quotient = dividend//divisor
    return div_quotient, int_div_quotient
r=division_integer_division(7,2)
print(r)


# to store multiple o/p separately
div_output1, div_output2 =division_integer_division(7, 2)
print(div_output1)
print(div_output2)

# calling one function inside another function
def add_mul(a, b):
    add_op=addition(a, b) 
    mul_op=multiplication(a, b)
    return add_op, mul_op
    
print(add_mul(5, 3))

