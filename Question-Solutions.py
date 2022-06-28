# Question 1
def print_song():
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!")
    print("\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")
    print("Twinkle, twinkle, little star,\n\tHow I wonder what you are")


# Question 2
def get_version():
    import sys

    print("Python Version -", sys.version[0:7])


# Question 3
def find_radius(radius: float):
    import math

    print("r =", radius)
    area = math.pi * (radius ** 2)
    print("Area =", area)


# Question 4
def print_name(first: str, last: str):
    print(last, first)


# Question 5
def number_list_styles(numbers: str):
    numbers = numbers.replace(",", "")
    num_list = list(numbers)
    num_tuple = tuple(numbers)
    print("List:", num_list)
    print("Tuple:", num_tuple)


# Question 6
def file_type(file: str):
    file = file.split(".")
    print(file[1])


# Question 7
def last_and_first(color_list: list):
    print(color_list[0] + ",", color_list[-1])


# Question 8
def exam_info(exam_st_date: tuple):
    print("The examination will start from:", str(exam_st_date[0]) + "/" + str(exam_st_date[1]) + "/"
          + str(exam_st_date[2]))


# Question 9
def number_addition(number: int):
    product = number + (number + number) + (number + number + number)
    print(product)


# Question 10
def print_calendar(month: int, year: int):
    import calendar

    for line in calendar.monthcalendar(year, month):
        print(line)


# Question 11
def find_volume(radius: float | int):
    import math
    volume = (4 / 3) * math.pi * (radius ** 3)
    print("Volume =", volume)


# Question 12
def abs_difference(number: float | int):
    difference = number - 17
    if str(difference)[0] == "-":
        print(abs(difference))
    else:
        print(difference * 2)


# Question 13
def close_to(number: float | int):
    if abs(2000 - number) <= 100 or abs(1000 - number) <= 100:
        print("True")
    else:
        print("False")


# Question 14
def add_or_multiply(n_one: float | int, n_two: float | int, n_three: float | int):
    if n_two == n_one:
        if n_one == n_three:
            total = (n_one + n_two + n_three) * 3
            print(total)
        else:
            total = n_one + n_two + n_three
            print(total)
    else:
        total = n_one + n_two + n_three
        print(total)


# Question 15
def copies_of_string(copies: int, string: str):
    print(string * copies)


# Question 16
def even_or_odd():
    number = int(input("Enter a number:\n-> "))
    remainder = number % 2
    if remainder == 1:
        print("The number is odd")
    else:
        print("The number is even")


# Question 17
def four_count(user_list: list):
    count = user_list.count(4)
    print(count)


# Question 18
def string_info(copies: int, string: str):
    if len(string) > 2:
        print(string[0:2] * copies)
    else:
        print(string * copies)


# Question 19
def is_vowel(letter: str):
    vowels = ("a", "e", "i", "o", "u")
    if letter in vowels:
        print("True")
    else:
        print("False")


# Question 20
def in_test(value, test_data: tuple):
    if value in test_data:
        print("True")
    else:
        print("False")


# Question 21
def multiples():
    for n in range(1500, 2701):
        if n % 7 == 0:
            if n % 5 == 0:
                print(n)


# Question 22
def concatenate(user_list: list):
    new_string = ""
    for n in user_list:
        new_string += str(n)
    print(new_string)


# Question 23
def print_even(numbers: list):
    for n in numbers:
        if n == 237:
            print(n)
            break
        elif n % 2 == 0:
            print(n)


# Question 24
def color_list_difference(color_list_1: list, color_list_2: list):
    color_list = []
    for n in color_list_1:
        if n not in color_list_2:
            color_list.append(n)
    print(color_list)


# Question 25
def triangle_area():
    base = float(input("Enter the base of the triangle:\n-> "))
    height = float(input("Enter the height of the triangle\n-> "))
    area = (base * height) / 2
    print(area)


# Question 26
def sum_three(n: int, x: int, y: int):
    if n == x or n == y or x == y:
        sum_num = 0
        print(sum)
    else:
        sum_num = n + x + y
    print(sum_num)


# Question 27
def sum_two(n: int, x: int):
    sum_num = n + x
    if 15 < sum_num < 20:
        print("20")
    else:
        print(sum_num)


# Question 28
def two_ints(n: int, x: int):
    if n == x or abs(n - x) == 5 or n + x == 5:
        print("True")
        return True


# Question 29
def add(object_one, object_two):
    if type(object_one) == int and type(object_two) == int:
        sum_objects = object_one + object_two
        print(sum_objects)


# Question 30
def personal_details(name: str, age: str, address: str):
    print("Name:", name, "\nAge:", age, "\nAddress:", address)


# Question 31
def algebra(x: float | int, y: float | int):
    solved = (x + y) ** 2
    print("({} + {}) ^ 2) = {}".format(x, y, solved))


# Question 32
def future_value_calc(amt: float | int, interest: float | int, years: float | int):
    future_value = round((amt * ((1 + (.01 * interest)) ** years)), 2)
    print(future_value)


# Question 33
def calc_distance(x1: float | int, x2: float | int, y1: float | int, y2: float | int):
    import math

    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    print(distance)


# Question 34
def sum_ints(n: int):
    result = (n * (n + 1)) / 2
    print(result)


# Question 35
def convert_to_cm(height: tuple):
    inches = (height[0] * 12) + height[1]
    cm = round((inches * 2.54), 2)
    print(cm)


# Question 36
def pythagorean(a: float | int, b: float | int):
    import math

    hypotenuse = round((math.sqrt((a ** 2) + (b ** 2))), 2)
    print(hypotenuse)


# Question 37
def convert_ft(ft: float | int):
    inches = ft * 12
    yards = round((ft / 3), 2)
    miles = round((ft / 5280), 2)
    print("Inches: {}\nYards: {}\nMiles: {}".format(inches, yards, miles))


# Question 38
def convert_to_sec(seconds=0, minutes=0, hours=0, days=0):
    day_sec = days * 3600 * 24
    hour_sec = hours * 3600
    min_sec = minutes * 60
    total_sec = day_sec + hour_sec + min_sec + seconds
    print("Total seconds is:", total_sec)


# Question 39
def convert_from_sec(seconds):
    day = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds = seconds % 3600
    minute = seconds // 60
    seconds = seconds % 60
    print("Days: {}\nHours: {}\nMinutes: {}\nSeconds: {}".format(day, hour, minute, seconds))


# Question 40
def calc_bmi(weight: float | int, height: float | int):
    bmi = round((weight / (height ** 2)), 2)
    print(bmi)


# Question 41
def convert_kpa(kpa: float | int):
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325
    print("Pressure in pounds per square inch: %.2f psi" % psi)
    print("Pressure in millimeters of mercury: %.2f mmhg" % mmhg)
    print("Atmospheric pressure: %.2f atm" % atm)


# Question 42
def sum_of_digits(number: str):
    num_list = []
    num_sum = 0
    for char in number:
        char = int(char)
        num_list.append(char)
    for num in num_list:
        num_sum += num
    print(num_sum)


# Question 43
def sort(n: int, x: int, y: int):
    new_list = [n, x, y]
    new_list.sort()
    print(new_list)


# Question 44
def gui_window():
    import tkinter as tk

    window = tk.Tk()
    window.wm_title("Practice GUI")
    window.mainloop()


# Question 45
def gui_label():
    import tkinter as tk

    window = tk.Tk()
    window.title("Practice GUI")

    label = tk.Label(master=window, text="Practice Label")
    label.grid(column=0, row=0)
    window.mainloop()


# Question 46
def gui_fancy_label():
    import tkinter as tk

    window = tk.Tk()
    window.title("Practice GUI")

    label = tk.Label(master=window, text="Practice Label", font=("Arial Bold", 30))
    label.grid(column=0, row=0)
    window.mainloop()


# Question 47
def gui_window_size():
    import tkinter as tk

    window = tk.Tk()
    window.wm_title("Practice GUI")
    window.geometry("300x300")
    window.mainloop()


# Question 48
def gui_window_resize_false():
    import tkinter as tk

    window = tk.Tk()
    window.wm_title("Practice GUI")
    window.geometry("300x300")
    window.resizable(False, False)
    window.mainloop()


# Question 49
def greater_than(num_list: list, num: int):
    counter = 0
    for n in num_list:
        if n <= num:
            counter += 1
    if counter == 0:
        print("True")
    else:
        print("False")


# Question 50
def print_equation():
    x = 30
    y = 20
    print("%d+%d=%d" % (x, y, x + y))
