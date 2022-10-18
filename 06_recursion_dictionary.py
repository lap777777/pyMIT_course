### recursion ... reducing problem to a sipler version of a problem = base case + recursive step

# klasicka iterativni verze
from re import A
from socket import AF_AAL5


def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(10, 10))

# rekurzivni verze
def mult(a, b):
    # base case
    if b == 1:
        return a
    # recursive step
    else:
        return a + mult(a, b-1)

print(mult(10, 10))
print()


# vypocet faktorialu:
def factorial(n):
    # base case:
    if n == 1:
        return 1
    # recursive step: reduce problem -> rewrite in terms of something simpler to reach base case:
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print()

# The towers of Hanoi
def printMove(fr, to):
    print("move from " + str(fr) + " to " + str(to))

def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n-1, fr, spare, to )
        towers(1, fr, to, spare)
        towers(n-1, spare, to, fr)


# Fibonacci rabbits
def fib(x):
    """
    assumes x and int >= 0
    returnes Fibonnaci of x
    """
    if x == 0 or x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


# palindrome - reads the same forwards and backwards
# first, convert the string to just characters, by stripping out puctuation and coverting upper case to lower case
# then:
# a) base case: a string of length 0 or 1 is a plindrome
# b) recursive case = if first char matches last char, then is a palidrome if middle section is a palindrome
def isPalindrom(s):

    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))

print(isPalindrom("abcdcba"))
print()


### Dictionary {key: value}
grades = {"Ana": "B", "John": "A+", "Denise": "A", "Katy": "A"}
# add:
grades["Sylvan"] = "A"
# test if key in dictionary:
"John" in grades
"Daniel" in grades
# delete entry
del(grades["Ana"])
# get an iterable that acts like a tuple of all keys
grades.keys()
# gen an iterable that acts like a tuple of all values
grades.values()

# creating a dictionary
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

# serazeni podle hodnot:
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)