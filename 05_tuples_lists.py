
### tuples ... immutable - nelze menit prvky
t1 = ()
t2 = (1,)
t3 = (2, "abc", 3.56)
t4 = t2 + t3
t4[-1]
t4[0:2]
len(t4)

# tuples used to swap variable values:
y = 1
x = 2
(x, y) = (y, x)
print(y, x)
print(x, y)
print()

# used to return more than one value from a function:
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return(q, r)
(quot, rem) = quotient_and_remainder(10, 3)
print(quot, rem)
print()


def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return(min_n, max_n, unique_words)
# aTuple: ((integer, string), (integer, string), (integer, string), ...)
# funkce bere cisla z tuplu a pridava je do cisel a bere stringy a pokud jsou unique, tak je dava do words a pak vraci 

test = ((1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "a"))
(min, max, words) = (get_data(test))
print("od:", min, "do:", max, "pismena:", words)
print()


### LISTS ... mutable - muzu je menit
# indices & ordering
a_list = []
my_list = [2, "a", 4, [1, 2]]
len(my_list)    # 4
my_list[0]      # 2
my_list[2] + 1  # 5
my_list[3]      # [1, 2]
i = 2
my_list[i-1]    # my_list[1] = "a"

# mutable
L = [2, 1, 3]
L[1] = 5
print(L)
print()

# iterating over a list - elements are indexed from 0 to len(L) - 1
total = 0
for i in range(len(L)):
    total += L[i]
print(total)

total = 0
for i in L:
    total += i
print(total)
print()

# operations on lists
L.append(5) # prida 5 na konec listu
L2 = [4, 5, 6]
L3 = L + L2

L3.extend([0, 6]) # prida 0 a 6 na konec listu
print()

L4 = [2, 1, 9, 2, 6, 7, 0]
del(L4[1])      # smaze 2. prvek listu, maze dle indexu
print(L4)
L4.pop()        # smaze posledni prvek listu
print(L4)
L4.remove(2)    # smaze prvni hodnotu 2 z listu
print(L4)
print()

# converting list to string and back
s = "I<3 cs"        # s is a string
l = list(s)         # l is a list, list meni string na list
print(l)
s3 = s.split("<")        # split rozdeli list dle zadaneho znaku
print(s3)
print(s)
L = ["a", "b", "c"]
s2 = " ".join(L)    # join udela z listu string
print(s2)
s3 = "_".join(L)
print(s3)
print()

L4 = [2, 1, 9, 2, 6, 7, 0]
L3 = [2, 1, 9, 2, 6, 7, 0]
L7 = sorted(L4)     # seradi list, nemeni ho
print(L7)
L3.sort()       # seradi list, ale zmeni ho
print(L3)
L3.reverse()    # opet meni list na nove poradi
print(L3)
print()

warm = ["blak", "blue", "red"]
hot = warm
hot.append("pink")
print(hot)
print(warm)
print()

# kdyz chci skopirovat list do noveho, ktery bude nezavisly
teply = hot[:]
teply.append("yellow")
print(teply)
print(hot)
print()


### cviceni 1.
def always_sunny(t1, t2):
    sun = ("sunny", "sun")
    first = t1[0] + t2[0]
    return (sun[0], first)

s = always_sunny(("cloudy"), ("cold",))
print(s)                # ("sunny", "ccold")
print()

### cviceni 2.
L = ["life", "answer", 42, 0]
for i in L:
    if i == 0:
        L[i] = "universe"
    elif i == 42:
        L[1] = "everything"

print(L)   # ["universe", "everything", 42, 0]
print()

### cviceni 3.
L1 = ["re"]
L2 = ["mi"]
L3 = ["do"]
L4 = L1 + L2        # ["re", "mi"]
L3.extend(L4)       # ["do", "re", "mi"]
L3.sort()           # ["do", "mi", "re"]
del(L3[0])          # ["mi", "re"]
L3.append(["fa", "la"]) # ["mi", "re", ["fa", "la"]]
print(L3)
print()

### cviceni 4.
L1 = ["bacon", "eggs"]
L2 = ["toast", "jam"]
brunch = L1
L1.append("juice")
brunch.extend(L2)    #["bacon", "eggs", "juice", "toast", "jam"]
print(brunch)









