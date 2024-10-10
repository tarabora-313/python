# functions programming

# High order function

def apply_twie(func, x):
    return func(func(x))

def add_five(x):
    return x + 5

result = apply_twie(add_five, 2)
print(result)        


# pure functions
students = 0
def sum(a, b):
    return a + b

result = sum(2, 3)
print(result)


# impure functions

student = []

def add_name(arg):
    student.append(arg)

add_name('Mohaid')

# is this impure or pure function
def func(x):
    y = x**2
    z = x + y
    return z

func(2)

# lambdas or anonymous function

result = (lambda x: x + 2)(23)

print(result)

def my_func(f, arg):
    return f(arg)

my_func(lambda x: 2*x*x, 5)    

def my_func\()

######################


