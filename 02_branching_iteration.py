### rozdil mezi + a , v printu, , pridava mezeru:

from re import A
from stringprep import b1_set


x = 1
x_str = str(x)

print("my number is", x, ".", "x=", x)
print("my number is", x_str + "." + "x=" + x_str)
print("my number is" + x_str + "." + "x=" + x_str)
print()

once = "umbr"
repeat = "ella"
u = once + (repeat+" ") *4
print(u)
print()


### input() .. vzdy vraci string
text = input("type in number: ")
print(text*5)
num = int(input("type in number: "))
print(num*5)
print()


### comparison operators >, <, >=, <=, !=, == ... 
print(5 > 3)
print("a" < "b")
print(5 != "a")
print(0 == False)
print()


### logic operations on booleans: not, and, or
a = True
b = not a
print(a)
print(b)
print()

pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)
print()

### conditions if, elif, else + identitation, nesting - jedna podminka strcena do druhe

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    if y != 0:
        print("x/y is", x/y)
    else:
        print("0/0")
elif x < y:
    print("x is smaller than y")
else:
    print("y is smaller than x")
print()


### loops
### while podminka: ... dela se tak dlouho, dokud plati true
n = 0
while n < 5:
    print(n)
    n = n + 1 #counter necessary for while
    # ctrl + c zastavi infinite loop
print()

n = input("You`re in the Lost Forest. Go left or right: ")
while n == "right" or n == "Right" or n == "RIGHT":
    n = input("You`re in the Lost Forest. Go left or right: " )
print("You got out of the Lost Forest!")
print()


### for x in range(start, stop, step): ... dela to dany pocet pokusu
my_sum = 0
for i in range(10, 20, 2):
    my_sum += i
    print(my_sum)
print()

# break - vyhodi me z loop (jak while, tak for)
# for pro dany pocet opakovani, while dokud neni podminka false, tak bezi, for potrebuje counter, while ho muze a nemusi mit

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)
print()