# Complete your individualized AI problems here
"""
def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"
"""

# 1 

name= "Anthony Loeza"
age=17

# 2

def check_number(num):
    if num>0:
        return "Positive"
    if num<0:
        return "Negative"
    else:
        return "Zero"

print(check_number(0))
print(check_number(2))
print(check_number(-4))

# 3

def sum_of(num1,num2):
    return num1+num2
print(sum_of(4,5))
print(sum_of(2,51))
print(sum_of(24,32))