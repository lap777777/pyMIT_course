
### first function

# function definition


def is_even(number):
    """
    Input: number, a positive int
    Returns True if number is even, otherwise False
    """
    return number % 2 == 0

# function call
is_even(10)
is_even(9)
print()


# scope ... enviroment - main program, funkce, ...

# global scope ... main program scope = funkce f
def f(x):
    x = x + 1
    print("in f(x): x=", x)
    return x

x = 3     # global variable
z = f(x)  # new scope - function scope
print(z)
print()

# pokud nezadam return do funkce, python vraci None type

def is_even_with_return(i):
    print("with return")
    remainder = i % 2
    return remainder == 0

is_even_with_return(3)
print(is_even_with_return(3))
print()


def is_even_without_return(i):
    print("without return")
    remainder = i % 2


is_even_without_return(3)
print(is_even_without_return(3))
print()


print("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
print()

# functions as arguments
def func_a():
    print("inside func_a")
def func_b(y):
    print("inside func_b")
    return y
def func_c(z):
    print("inside func_c")
    return z()

print(func_a())
print(5 + func_b(2))
print(func_c(func_a))
print()

# scope details
def g(x):
    def h():
        x = "abc"
    x = x + 1
    print("g: x =", x)
    h()
    return x

x = 3
z = g(x)
print()


# cviceni 1:
def add(x, y):
    return x + y

def mult(x, y):
    print(x*y)

# kolik radku kodu se zobrazi
add(1,2)          # 0
print(add(2,3))   # 1: 5
mult(3,4)         # 1: 12
print(mult(4,5))  # 2: 20, None
print()


# cviceni 2:
def sq(func, x):
    y = x**2          # 4
    return func(y)

def f(x):
    return x**2       # 16

calc = sq(f, 2)
print(calc)
print()







