def excersice_1():
    name = input("Whats your Name!")
    age = int(input("How old are you!"))
    is_new = input("Are you new Here!")
    if name == "John Smith" and age == 20:
        print(f" Name is {name}\n He is {age} old\n He is a new patient.")


def excersice_2():
    num_1 = float(input("Write a First number! "))
    num_2 = float(input("Write a Second number! "))
    return num_1 + num_2


# print(f"Sum is : {excersice_2()}")
def excersice_3():
    weight = int(input("Weight :"))
    in_kg_or_pound = input("(K)g or (L)bs: ").lower()
    kg = int()
    lbs = float()
    if in_kg_or_pound != 'k':
        kg = weight * 0.45
        print(kg)
    elif in_kg_or_pound == "k":
        lbs = weight / 0.45
        print(lbs)


# excersice_3()

def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# print(maximum(2,8))

def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)


# fizz_buzz(45)

def speed_check(speed):
    demerit_point = 0
    over_speed = 0
    if speed < 70:
        print("OK")
    elif speed > 70:
        over_speed = speed - 70
        demerit_point = over_speed // 5
        print(f"Points : {demerit_point}.")
        if demerit_point > 12:
            print("License is suspended")


# speed_check(200)

def even_odd(limit):
    for num in range(limit):
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")


# even_odd(20)

def sum_of_multiples(limit):
    for num in range(1, limit + 1):
        if (num % 3 == 0) or (num % 5 == 0):
            print(num)


# sum_of_multiples(20)

def show_stars_in_rows(limit):
    for num in range(1, limit + 1):
        print(num * "*")


# show_stars_in_rows(5)

def prime_number(limit):
    for num in range(1, limit + 1):
        if (num == 2) or (num == 3) or (num == 5):
            print(num)
        elif (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
            continue
        else:
            print(num)


# prime_number(100)

