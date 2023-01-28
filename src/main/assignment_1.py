import math as math


# Question 1
# The current binary code we have is a 64 bit digit. Let's break it down into three sections: sign, exponent, and fraction

sign = 0
exponent = [1,0,0,0,0,0,0,0,1,1,1]
fraction = [1,1,1,0,1,0,1,1,1,0,0,1]

# This determines the value for c
count1 = 0
c = 0
while count1 < 11:
    if exponent[count1] == 1:
        c = c + (2**(10 - count1))
    count1 += 1

# This determines the value for f
count2 = 0
f = 0
while count2 < 12:
    if fraction[count2] == 1:
        f = f + ((1/2)**(count2 + 1))
    count2 += 1

variable = (-1) ** (sign) * (2 ** (c - 1023)) * (1 + f)
print("Question 1: " + "%.5f" % variable + "\n")


# Question 2
norm1 = variable * (10 ** -3)
print("Question 2: " +  str((math.floor(norm1 * 1000))) + "\n")


# Question 3
norm = variable * (10 ** -3)
norm = round(norm, 3)
print("Question 3: " + str(norm * 1000) + "\n")

# Question 4
norm1 = norm * (10 ** 3)
def absolute_error(precise: float, approximate: float):
    num = abs(precise - approximate)
    return num 
def  relative_error(precise: float, approximate: float):
    num = (abs(precise - approximate)/ abs(precise))
    return num
print("Question 4 (absolute error): " + str(absolute_error(variable, norm1)) )
print("Question 4 (relative error): " + str(relative_error(variable, norm1)) + "\n\n")

# Question 5
x = 1
k = 1

def check_if_alternating(function: str):
    if "(-1) ** k" in function:
        return True
    return False

def check_if_decreasing(function: str, x: int):
    k = 1
    start_value = abs(eval(function))
    for k in range(2, 10000):
        result = abs(eval(function))
        if start_value <= result:
            return False
    return True

function = "((-1) ** k) * ((x ** k)/(k ** 3))"

def infinite_series(x: int, k: int):
    return ((-1) ** k) * ((x ** k )/ (k ** 3))
err_tol = 10 ** -4
current_iteration = 1
while(abs(infinite_series(1, current_iteration)) > err_tol):
    current_iteration += 1
current_iteration = current_iteration - 1

if check_if_alternating(function) == True and check_if_decreasing(function,x) == True:
    infinite_series(x,k)
    print("Question 5: " + str(current_iteration) + "\n")

# Question 6a
a = -4
b = 7
def bisection_method(left: float, right: float, function1: str):
    x = left
    initial_left = eval(function1)
    x = right
    initial_right = eval(function1)
    if initial_left * initial_right >= 0:
        print("Invalid inputs. Not on opposite sides of function")
        return
    err_tol = 10**-4
    diff: float = right - left
    iteration_count = 0
    max_iteration = 20
    while(diff >= err_tol and iteration_count < max_iteration):
        iteration_count += 1
        mid = (right + left) / 2
        x = mid
        eval_mid = eval(function1)
    
        x = left
        eval_left = eval(function1)
        condition1: bool = eval_left < 0 and eval_mid > 0
        condition2: bool = eval_left > 0 and eval_mid < 0

        if condition1 == True or condition2 == True:
            right = mid
        else:
            left = mid
        diff = abs(right - left)
    return iteration_count

def deriv(value):
    return (3 * value * value) + (8 * value)
def newton_method(initial_approximation: float, sequence: str):
    iter_count = 0
    tol = 10 ** -4
    x = initial_approximation
    f = eval(sequence)
    f_prime = deriv(initial_approximation)
    approximate: float = f / f_prime
    while(abs(approximate) >= tol):
        x = initial_approximation
        f = eval(sequence)
        f_prime = deriv(initial_approximation)
        
        approximate = f / f_prime
        initial_approximation -= approximate
        iter_count += 1
    return iter_count

function = "(x**3) + (4 * x * x) - 10"
    
print("Question 6a (bisection method): " + str(bisection_method(a,b,function)))
print("Question 6b (Newton's method): " + str(newton_method(-4,function)))










