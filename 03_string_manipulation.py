s = "abcdefg"
delka = len(s)
print(delka)
print()

# indexing
print(s[0])
print(s[1])
print(s[2])
print(s[-1])
print(s[-2])
print(s[-3])
print()

# slicing [start:stop:step]
print(s[1:6:2])
print(s[:])
print(s[::-1])
print()

# strings are "immutable" ... nemuze byt prepsat
s = "hello"
#s[0] = "y"  # vyhodi chybu
s = "y" + s[1:]  # nahrazeni puvodniho stringu s y
print(s)
print()

# for loop + strings
s = "abcudefghi"
for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("There is an i or u.")

for char in s:
    if char == "i" or char == "u":
        print("There is an i or u.")
print()

# Guess and checks
cube = 8
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
print()

# Approximate solution
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.005
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print("num_guesses =", num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)
print()

# bisection search ... vylucuji polovinu populace
import random

no = random.randint(1, 100)

guess = 101
while no != guess:
    guess = int(input("Hadej cislo od 1 do 100: "))
    if guess > no:
        print("Hledane cislo je mensi nez tvuj tip.")
    elif guess < no:
        print("Hledane cislo je vetsi nez tvuj tip.")
print("Vyborne, nasel jsi hledane cislo", no)
print()

# cviceni 1
s = "6.00 is 6.0001 and 6.0002"
new_str = ""
new_str += s[-1]  #2
new_str += s[0]   #26
new_str += s[4::30]   #26_
new_str += s[13:10:-1]   #26 100
print(new_str)
print()

# cviceni 2
round = 0
s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            round += 1
            print("round:", round, char1, char2)
            if char1 == char2:
                print("common letter")
print()




