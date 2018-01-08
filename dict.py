def print_sunny():
    print("its a sunny and warm day")
def print_rainy():
    print("its a rainy and glommy day")
def print_snowy():
    print("its a snowy and cold day")
def default():
    print("Oops this is mistake")

switch = {
    "1":print_sunny,
    "2":print_rainy,
    "3":print_snowy
}

inp = input("Enter choice")

try:
    switch[inp]()
except:
    default()
finally:
    print("enter the choice again")