### debuging
# defensive programming
# - write specificatins for functions
# - modularize programs
# - check conditions on inputs/outputs
# - tests
#   a) unit testings - testing each function separately, validate each piece of program
#   b) regresion testing - add test for bugs as you find them, catch reintroduced errors that were previously fixed
#   c) integration testing - test program as a whole

# testovat hranicni hodnoty (podminky), 
# loop - nevstoupi, vstoupi jednou, vstoupi vickrat, u while kdy se vypadne ze smycky, breaky
# print() statement vyuziti pro kontrolu v jednotlivych castech programu


# Error messages - exceptions:
# try block - provedene se, pokud neni chyba
# except - pokud je v try blocku chyba, skoci se do except bloku
# else - provede se po try bloku, pokud v nem neni chyba
# finally - vzdy se provede po try, else a except clauses - i kdyz je tam break, return apod. - pouziti pro vycisteni kodu bez ohledu na to, co se stalo = napr. pro zavreni souboru

try:
    a = int(input("Tell mi one number: "))
    b = int(input("Tell mi another number: "))
    print("a/b = ", a/b)

except ValueError:
    print("Cound not convert to a number.")
except ZeroDivisionError:
    print("Cannot divide by 0.")
except:
    print("Something went very wrong.")
else:
    print("a+b = ", a+b)
finally:
    print("And that`s all folks.")
print()


# raise your own exception
# raise Exception("descriptive string")

def get_ratios(L1, L2):
    """
    Assumes: L1 and L2 are lists of equal lenght of numbers.
    Returns: a lit containing L1[i]/L2[i]
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float("nan"))  #nan = not a number
        except:
            raise ValueError("get_ratios() called with bad arg/")
    return ratios


def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    return sum(grades)/len(grades)

# pokud je list se znamkami prazdny, len(grades) = 0 a vypadne ZeroDivisionError

# reseni a) - flag error = print statement:
def avg2(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("Warning: no grades data!")
        # funkce vraci None

# reseni b) - change of policy (default value - zapisu do doctringu)
def avg3(grades):
    """
    Returns average value of grades.
    If there are no grades, returs 0
    """
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("Warning: no grades data!")
        return 0.0


### Assertions
# do programu pridat "nutne podminky" pro spravny beh ve formatu:
# assert podminka, "print chybove hlasky"
def avg4(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades) / len(grades)

# raises AssertionError if it is given an empty list for grades
# otherwise runs ok

my_list = [1, 2, 3, 4]
my_list2 = []
x = avg4(my_list)
print(x)
y = avg4(my_list2)
print(y)
print()

# assertion pouzit u:
# - check types of arguments or values
# - check that invariants on data structrues are met
# - check constraints on return values
# - 

# cviceni
def is_even(n):
    """
    returns True if a number is even and False if not
    """
    if n > 0 and n % 2 == 0:
        return True
    elif n < 0 and n % 2 == 0:
        return True
    else:
        return False

# program neresi 0


# cviceni2
L = 3
for i in range(len(L)):
    print(i)

# L neni list, ale integer a na nem nemuzu volat len() funkci


# cviceni3
try:
    n = int(input("How old are you: "))
    percent = round(n*100/80, 1)
    print("You`ve gone through", percent, "% of your life!")
except ValueError:
    print("Oops, you must enter a number.")
except ZeroDivisionError:
    print("Division by zero.")
except:
    print("Something went very wrong.")

# if user enteres twenty - dostanu zpet Value error: "Oops, ..."
