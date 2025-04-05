# #Variables-kontener przechowujący dane

# #string
# name = "Jakub"
# email = "kubadewerendaa@gmai.com"

# #integer
# age = 21

# #float 
# price = 10.99

# #boolean
# is_student = False

# print(f"Hello my name is {name} and I am {age}")

# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")


# #Typecasting-konwersja zmiennych

# name = "Jakub"
# age = 21
# gpa = 4.5
# is_student = True

# age = float(age)
# print(age)

# gpa = int(gpa)
# print(gpa)

# #Input-pobieranie danych od użytkownika

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))

# age = age + 1
# print(f"Hello {name}, your age is {age}")


# #Exc 1 Rectangle area calc 
# lenght = float(input("Ente the lenght of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = lenght * width

# print(f"The area of the rectangle is {area}")

# #if statement-jeżeli

# age = -1

# if age >= 18:
#     print("You are signed in")
# elif age < 0:
#     print("You are not born yet")
# else:
#     print("You must be 18+ to sign in")

# # Exc 2 calculator
# operation = input("Enter opaerator (+ - * /): ")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     rersult = num1 / num2
# else:
#     print(f"The operator {operation} is not recognized")

# print(f"The result is {round(result, 3)}")#zaokrąglenie do 3 miejsc po przecinku

# #temperatur cenvertion
# unit = input("Is this temp in C or F?: ").lower()
# temp = int(input("Enter the temp: "))

# if unit == "c":
#     temp = round((temp * 9) / 5 +32 , 2)
#     print("Temp in F is: ", temp)
# elif unit == "f":
#     temp = round((temp - 32) * 5 / 9, 2)
#     print("Temp in C is: ", temp)
# else:
#     print(f"The unit {unit} is not recognized")

# #Conditionals expressions

# result = "Even" if 11 % 2 == 0 else "Odd"

# a = 10
# b = 11

# min_num = a if a < b else b
# max_num = a if a > b else b 


# print(result)

# #String methods

# name = "Jakub"
# # result = len(name)
# result = name.find("k")#rfind-szuka od końca
# result = name.capitalize()#Pierwsza litera duża
# result = name.upper()
# result = name.lower()
# result = name.isdigit()#sprawdza czy string jest liczbą i zwraca True jesli jest
# result = name.isalpha()#sprawdza czy string jest literą i zwraca True jesli jest
# result = name.count("a")#zlicza ile razy występuje litera w stringu
# result = name.replace("a", "e")#zamienia litery
# print(result)

# #Exc 3 validate user input
# username = input("Enter username: ")

# if len(username) > 12:
#     print("Username must be max 12 characters")
# elif not username.find(" ") == -1:
#     print("Username cannot contain spaces")
# elif not username.isalpha():
#     print("Username can only contain letters")
# else:
#     print(f"Welcome {username}")

# #Indexing [start : end : step]
# credit_num = "1234-5678-9012-3456"

# print(credit_num[0])
# print(credit_num[:4])
# print(credit_num[5:9])
# print(credit_num[5:])
# print(credit_num[-1])#ostatni znak
# print(credit_num[-4])#czwarty znak od końca
# print(credit_num[::2])#co drugi znak
# print(credit_num[::-1])#odwrócenie stringu

# last_digits = credit_num[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# #format specs
# price = 1000.99

# print(f"Price: ${price:.3f}")
# print(f"Price: ${price:010}")#dopełnienie zerami
# print(f"Price: ${price:010.2f}")#dopełnienie zerami i 2 miejsca po przecinku
# print(f"Price: ${price:<10}")#wyrównanie do lewej
# print(f"Price: ${price:>10}")#wyrównanie do prawej
# print(f"Price: ${price:^10}")#wyrównanie do środk
# print(f"Price: ${price:+}")#dodatnia wartość
# print(f"Price: ${price: }")#odsep dla poz
# print(f"Price: ${price:+,.3f}")

# #while loop
# name = input("Enter your name: ")

# # if name == "":
# #     print("Empty name")
# # else:
# #     print(f"Hello {name}")

# while name == "":
#     print("Dont leave empty name!")
#     name = input("Enter your name once again!: ")

# print(f"Hello {name}")

# num = int(input("Enter number beetwen 1 and 10: "))

# while num < 1 or num > 10:
#     print("Number out of range")
#     num = int(input("Enter number beetwen 1 and 10 "))

# print(f"Your number is {num}")

# #for loops
# for x in reversed(range(1, 11, 2)):#odwrotynie
#     print(x)

# print("happy new year!")

# credit_card = "1234-5678-9012-3456"

# for i in credit_card:
#     print(i)

# for i in range(1,21):
#     if i == 13:
#         continue
#     else:
#         print(i)


# #Exc 4 clock

# import time

# time.sleep(3)

# print("time is up!")

# import time

# time_c = int(input("Enter your time in secounds: "))

# for x in range(time_c, 0, -1):
#     secounds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{secounds:02}")
#     time.sleep(1)

# print("Time is up!")

# #nested loop
# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")

# # collections
# # list[]-kolekcja elementów
# # set{}-unikalne elementy, mozna dodawac i usowac, nie ma indexowania
# # touple()-niezmienne dane,szybsza niz lista 
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# print(fruits[::-1])

# fruits.append("fig")
# fruits.remove("banana")
# fruits.insert(1, "blueberry")
# fruits.sort()
# fruits.reverse()
# fruits.index("apple")
# fruits.pop()#usuwa ostatni element

# for fruit in fruits:
#     print(fruit)

# num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# #Dicionaries
# capitals = {
#     "USA": "Washington DC",
#     "France": "Paris",
#     "Germany": "Berlin",
#     "Poland": "Warsaw"
# }

# print(capitals.get("USA"))

# capitals.update({"Spain": "Madrid"})
# capitals.update({"Poland": "Kraków"})#update zmienia wartość, oraz dodaje nowa
# # capitals.pop("France")
# # capitals.popitem()#usuwa ostatni element

# print(capitals.keys())#klucze
# print(capitals.values())#wartości

# for key in capitals.keys():
#     print(key)

# items = capitals.items()#zwraca tuple

# for key, value in capitals.items():
#     print(f"{key} : {value}")

# print(capitals)

# #Concesion ctand program

# menu = {
#     "pizza": 10.99,
#     "salad": 5.99,
#     "soup": 3.99,
#     "bread": 2.99,
#     "water": 1.99,
#     "coke": 1.50
# }

# card = []

# total = 0

# print("------ MENU ------")
# for key, value in menu.items():
#     print(f"{key:10} : ${value:.2f}")

# print("------------------") 

# while True:
#     food = input("Select what do u wanna buy(q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         card.append(food)

# print("--- YOUR ORDER ---") 

# for food in card:
#     total += menu.get(food)
# print(f"Total is: ${total}")

# import random

# low = 1
# high = 100

# options = ("rock", "paper", "scisors")
# cards = ["1","5","32","Q","2","J"]

# number = random.randint(low, high)
# number = random.random()#random float 0-1
# option = random.choice(options)
# random.shuffle(cards)#randomowo miesza

# print(cards)

# #functions
# def happy_birthday(name):
#     print(f"Happy birthday {name}")

# happy_birthday("benek")

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Benek", 42.50, "01/01")

# def multiply(x, y):
#     return x*y

# print(multiply(2, 2)) 
# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# import time

# def count(end, start=0):
#     for x in range(start, end):
#         print(x)
#         time.sleep(1)

#     print("DONE!")

# count(10)

# #keywardargs
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")

# hello("Hello", title="Mr.", last="Snow", first="John")

# #*ARGS
# def add(*nums):#*args tio samo
#     total = 0
#     for x in nums:
#         total += x
#     return total

# print(add(1, 2, 3))

# #**KWARGS
# def print_addres(**kwargs):#zmienne cale jakby dict
#     for key,value in kwargs.items():
#         print(f"{key:10} : {value}")

# print_addres(street="Tadiego Kosciuszki",apartment=68, city="Krakow",zip="31-114")

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for key, value in kwargs.items():
#         print(f"{key:10} : {value}")

# shipping_label("Dr.", "Benek", "Snow", 
#                street="Tadeusza Kosciuszki",
#                city="Kraków",
#                zip="31-114"
#                )
# #ITERABLES- MOozna chodzic po nich w petli i je zwracac

# # Membership operators
# word = "apple"
# letter = "apple pie"

# if word in letter:
#     print("yes")
# else:
#     print("no")

# email = "kubadewerendaa@gmail.com"

# if "@" in email and "." in email:
#     print("It is a email")
# else:
#     print("Wrong email!")

# doubles = [x * 2 for x in range(1,11)]#działanie for item in warunek

# triples = [y * 3 for y in range(1,11)]

# print(doubles)
# print(triples)

# fruits = ["apple", "banana", "berry"]
# fruits_chars = [fruit[0] for fruit in fruits]

# print(fruits_chars)

# numbers = [1, 2, -3, 6,-2]

# psoitive_num = [num for num in numbers if num >= 0]
# print(psoitive_num)

# #Macth-case statement alternatywa dla if-elif-else
# def day_of_week(day):
#     if day == 1:
#         return "Sunday"
#     elif day == 2:
#         return "Monday"
#     elif day == 3:
#         return "Tuesday"
#     elif day == 4:
#         return "Wednesday"
#     elif day == 5:
#         return "Thursday"
#     elif day == 6:
#         return "Friday"
#     elif day == 7:
#         return "Saturday"
#     else:
#         return "Invalid day"

# print(day_of_week(1))

# def day_of_week(day):
#     match day:
#         case 1:
#             return "Sunday"
#         case 2:
#             return "Monday"
#         case 3:
#             return "Tuesday"
#         case 4:
#             return "Wednesday"
#         case 5:
#             return "Thursday"
#         case 6:
#             return "Friday"
#         case 7:
#             return "Saturday"
#         case _:#cos typu else
#             return "Invalid day"

# print(day_of_week(1))

# #Module import
# #import math as m
# from math import pi
# print(pi)

# # variable scope- widocznosc zmiennych 
# # global - globalne zmienne
# # nonlocal - zmienne lokalne w funkcji
# #LEGB - Local, Enclosing, Global, Built-in

# #if __name__ == "__main__":#sprawdza czy plik jest uruchamiany jako glowny

# def main():
#     # program
#     print(__name__)

# if __name__ == '__main__':
#     main()

# #Python Bank Progrtam   

# def show_balance(balance):
#     print(f"-----Your balance is ${balance:.2f}-----")

# def deposit():
#     amount = float(input("Enter an amount to be deposited: "))

#     if amount < 0:
#         print("That's not valid amount")
#         return 0
#     else:
#         return amount
    
# def withdraw(balance):
#     amount = float(input("Enter amount to withdraw: "))

#     if amount > balance:
#         print("Not enought balance")
#         return 0
#     elif amount < 0:
#         print("Amount must be > 0")
#         return 0 
#     else:
#         return amount

# def main():
#     balance = 0 
#     is_running = True

#     while is_running:
#         print("Banking Program")
#         print("1. Show Balance")
#         print("2. Deposit")
#         print("3. Witchdraw")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         match choice:
#             case "1":
#                 show_balance(balance)
#             case "2":
#                 balance += deposit()
#             case "3":
#                 balance -= withdraw(balance)
#             case "4":
#                 is_running = False
#             case _: 
#                 print("-----Invalid choice!-----")
            
#     print("Thank you :)")

# if __name__ == "__main__":
#     main()

# #Encriptiong
# import random
# import string

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()


# random.shuffle(key)

# # print(f"chars: {chars}")
# # print(f"key: {key}")

# #Encrypting
# plain_text = input("Enter message to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"original message: {plain_text}")
# print(f"encrypted message: {cipher_text}")

# #Decrypting
# cipher_text = input("Enter message to encrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f"encrypted message: {cipher_text}")
# print(f"original message: {plain_text}")

# #Hangman
# import random

# words = ("apple", "orange", "banana", "coconut", "pineapple")

# #dict of kley:()
# hangman_art = {0: ("    ",
#                    "    ",
#                    "    "),
#                1: ("  o  ",
#                    "     ",
#                    "     "),
#                2: ("  o  ",
#                    "  |  ",
#                    "     "),
#                3: ("  o  ",
#                    " /|  ",
#                    "     "),
#                4: ("  o  ",
#                    " /|\\ ",
#                    "     "),
#                5: ("  o  ",
#                    " /|\\ ",
#                    " /   "),
#                6: ("  o  ",
#                    " /|\\ ",
#                    " / \\ "),
#                }

# def display_man(wrong_guesses):
#     print("*"*15)
#     for line in hangman_art[wrong_guesses]:
#         print(line)

# def display_hint(hint):
#     print(" ".join(hint))# elementy hint oddzielone spacja

# def display_answer(answer):
#     print(" ".join(answer))

# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer) 
#     wrong_guesses = 0
#     guessed_letters = set()
#     is_running = True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)

#         guess = input("Enter a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input")
#             continue

#         if guess in guessed_letters:
#             print(f"{guess} is already guessed")
#             continue

#         guessed_letters.add(guess)

#         if guess in answer:
#             for index in range(len(answer)):
#                 if answer[index] == guess:
#                     hint[index] = guess   
#         else:
#             wrong_guesses += 1

#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You WIN!")
#             is_running = False
#         elif wrong_guesses >= len(hangman_art) - 1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You LOOSE!")
#             is_running = False

# if __name__ == "__main__":
#     main()

#Programowanie objektowe 
# - class struktura 
# - atribute zmienne
# - methods fukncje

# class Car:
#     def __init__(self, model, year, color, for_sale):#__ dunder
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
# from car import Car

# car1 = Car("BMW", 2024, "black", False)
# car2 = Car("Merol", 2022, "white", True)

# print(car1.model)
# print(car1.for_sale)
# print(car2.model)
# print(car2.for_sale)

# car2.stop()
# car1.drive()

# car1.drive()
# car1.stop()

# car2.dsecribe()

#class variables = dostepne pomiedzy wszystkimi metodami itp klasy przyklad
# class Car:
#     wheels = 4
#     def __init__(self):
#         pass

# class Student:
#     class_year = 2024
#     num_students = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1#zliczamy w ten sposob ile obiektow powstalo

# student1 = Student("Ben10", 10)
# student2 = Student("Patrick", 35)
# student3 = Student("Sandy", 32)

# print(student1.name)
# print(student1.age)
# print(student1.class_year)#class variables daja nam dostep do kazdego student i class_year moze byc
# #tez 
# print(Student.class_year)
# print(Student.num_students)

# print(f"My graduading class of {Student.class_year} has {Student.num_students} students")
# print(student1.name)
# print(student2.name)
# print(student3.name)

# #Inharitance = dziedziczenie z klasy do klasy metod i atrybutow
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MOEW!")
        
# class Mouse(Animal):
#     def speak(self):
#         print("SQUEEK!")

# dog = Dog("Scooby")
# cat = Cat("Tom")
# mouse = Mouse("Jerry")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()
# cat.speak()

# # Date & times
# import datetime

# date = datetime.date(2025, 1, 2)
# today = datetime.date.today()

# time = datetime.time(12, 30, 0)

# now = datetime.datetime.now()

# now = now.strftime("%H:%M:%S %d-%m-%Y")

# print(date, today, time)
# print(now)

# target_datetime = datetime.datetime(2010, 1, 2, 12, 30, 1)
# current_datetime = datetime.datetime.now()

# if current_datetime > target_datetime:
#     print("Target date has passed")
# else:
#     print("Target date has not passed")

# # Python Alarm clock
# #file alarmclock.py

# # multithreading = kilka zadanb w tym samym czasie, dobre dla fetchowania api

# import threading
# import time

# def walk_dog(first, last):
#     time.sleep(8)
#     print(f"You finished walking the {first} {last}")

# def take_out_thrash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(4)
#     print("You get the mail")

# walk_dog("Soltys", "dog")
# take_out_thrash()
# get_mail()

# chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))#, jesli 1 arg zeby bylo wiadome ze tuple, 
#                                                  #oraz za pomoca args sie daje argumenty do funkcji w thread
# chore1.start()

# chore2 = threading.Thread(target=take_out_thrash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are complete!")

# # Łączenie z API python

# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failded to retrieve data {response.status_code}")

# pokemon_name = "typhlosion"

# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")

# #multilevel inharitance = dziedziczenie od rodzicow odbywa 
# # sie c(b) <= b(a) <= a
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat(self):
#         print(f"{self.name} is eating")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Soltys")
# hawk = Hawk("Tony")
# fish = Fish("Endrju")

# fish.hunt()
# rabbit.eat()

# #super() = klasa ktora pozwala na dziedizczeni metod z rodzica
# #Pozwala nam przedluzyc funkcjonalnosc odziedzizonej metody
# class Shape:
#     def __init__(self, color, field):
#         self.color = color
#         self.field = field

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.field else 'not filled'}")

# class Circle(Shape):
#     def __init__(self, color, field, radius):
#         super().__init__(color, field)
#         self.radius = radius

#     def describe(self):
#         print(f"It is a circle with area of {3.14 * self.radius ** 2}")
#         super().describe()

# class Square(Shape):
#     def __init__(self, color, field, width):
#         super().__init__(color, field)
#         self.width = width

# class Triangle(Shape):
#     def __init__(self, color, field, width, height):
#         super().__init__(color, field)
#         self.width = width
#         self.height = height

# circle = Circle("red", True, radius=5)
# triangle = Triangle("black", True, 7, 8)

# print(triangle.color)
# print(triangle.field)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")

# circle.describe()

# #polymorphism = tzw wiele form, czyli moze byc uzywana w wielu przypadkach
# #osiagnac mozna przez: dziedziczenie
# #"duck typing"

# from abc import ABC, abstractmethod

# class Shape:

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base 
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.radius = radius

# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("peperoni", 15)]

# for shape in shapes:
#     print(shape.area())

# #"Duck  Typing" = Jezeli wyglada jak kacza i gdacze jak kaczak to musi byc kaczka
# #czyli jezeli dany oiekt ma jakies klasy co chcemy od niego odziedizczyc ale np nie jest 
# #   tak jak nizej tylko carem to mozemy 
# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# class Car:
#     alive = False
#     def speak(self):#to nie zwierze ale dajemy speak bo gada jak kaczka wi jest kaczka
#         print("Honk!")
    
# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)

# #static methods = metoda nalezaca bardziej do klasy niz do obiektu

# #instance method
# def get_info(self):
#     return f"{self.name} = {self.position}"

# @staticmethod = metoda, ktora nie bierze danych z klasy
# def km_to_milets(kilometers):
#     return kilometers * 0.621371

# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position

#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
#         return position in valid_positions

# print(Employee.is_valid_position("Football"))# Nalezy do klasy a nie do obiektu stworzonego przez klase

# #class methods = sa to metody klasy zamiast (self) pierwszy arg to (cls)===========================================

# class Student:
#     count = 0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
    
#     #Instance methods
#     def get_info(self):
#         return f"ID: {self.name} {self.gpa}"
    
#     @classmethod
#     def get_count(cls):
#         return f"Total number of students: {cls.count}"
    
#     @classmethod
#     def get_total_avg(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"AVG: {cls.total_gpa/cls.count:.2f}"
    
# student1 = Student("Spangebob", 3.2)
# student2 = Student("Ben", 4.2)
# student3 = Student("Money", 2.2)

# print(Student.get_count())
# print(Student.get_total_avg())

# #Magic methods = dunder methods __init__, __str__ itp
# #mozemy definiowac wlasnie zachowania

# class Book:
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):#print
#         return f"'{self.title}' by {self.author}"
    
#     def __eq__(self, other):#porowananie 2 obiektow
#         return self.title == other.title and self.author == other.author

#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
    
#     def __add__(self, other):
#         return self.num_pages + other.num_pages
    
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
    
#     def __getitem_(self, key):
#         if key == "title":
#             return self.title
# book1 = Book("NFS", "J.R.R", 310)
# book2 = Book("NFS", "J.R.R", 550)
# book3 = Book("KGB", ".R", 100)

# print(book1)#<__main__.Book object at 0x0000026BBA9DA420> = przed __str__
# #'NFS' by J.R.R po uzyciu __str__
# print(book1 == book2)
# print(book1 + book2)
# print("NFS" in book2)#contains
# print(book2['title'])

#@property = metoda do ktorej jest dostep jak do atrybutu 
# daje getter, setter i deleter
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width#czyli prywatne, do uzywania tylko w klasie
#         self._height = height
    
#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"
    
#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
    
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Musi byc > 0")
    
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Musi byc > 0")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Usunieto")

# rectangle = Rectangle(3, 4)

# #setter===========================================
# rectangle.width = 0# blad

# #getter===========================================
# print(rectangle.width)
# print(rectangle.height)

# #deleter===========================================
# del rectangle.width

# #Decorators = zmienia dzialanie fukncji bez zmianiania jej kodu
# def add_sparkles(func):
#     def wrapper(*args, **kwargs):#to potrzebne bo wtedy add_sparkles decorator jest 
#         #wywolywany gdy wywolujemy tez get_ice_cram, 
#         # a bez tego bylby porpostu po @add_sparkles
#         print("You have sparkles also")
#         func(*args, **kwargs)
#     return wrapper

# def add_funct(func):
#     def wrapper(*args, **kwargs):#*args, **kwargs to musi byc gdy wrappowana 
#         #funckja przyjmuje jakies argumenty
#         print("You added funct")
#         func(*args, **kwargs)
#     return wrapper

# @add_funct
# @add_sparkles
# def get_ice_cream(flavor):
#     print(f"There is your {flavor} ice cream")

# get_ice_cream("vanilla")

# #Exception = Bledy ktore zatrzymuja dzialanie programu
# # (ZeroDivisionError, TypeError, ValueError)
# # try except finally

# #int("pizza") ValueError
# try:
#     number = int(input("Enter number: "))
#     print(1/number)
# except ZeroDivisionError:
#     print("Cant divide by 0")
# except ValueError:
#     print("Enter only number pls")
# except Exception:#wszystkie bledy
#     print("Something went wrong")
# finally:#Zawsze sie robi
#     print("Do some cleanup there")


# ===========================================#Python file detection===========================================
# import os

# #relative test.txt
# file_path = "test.txt"
# #absolute
# #file_patch = "C:\Users\kubad\OneDrive\Pulpit\Programowanie\Python\test.txt" tylko zamienic \ na /

# if os.path.exists(file_path):
#     print("the location exists")
#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("that is a directory folder")
    
# else:
#     print("That loation doesnt exists")

# #Writing files .txt .json .csv
# txt_data = ["Eugene", "Benek", "Marop", "Zenon"]

# import json
# import csv

# employee = {
#     "name": "Ben",
#     "age": 21,
#     "job": "Programmer"
# }

# employees = [["Name", "Age", "Job"],
#              ["Benek", 21, "Programmer"],
#              ["Patric", 37, "Cook"],
#              ["Sandy", 27, "Scientists"]]


# file_path = "output.txt"

# try:
#     with open(file_path, "w",newline="") as file:#to with open otwiera nam plik file patch jako
#     # w- write i go zamyka odrazu po tym co ma zrobic w with open
#                                    # cos jak try finally
#     #x tez do zapisu ale wykrywa czy juz istnieje
#     #a dodaje na koniec
#         #--------------------LISTA
#         # for employe in txt_data:
#         #     file.write(employe + " ")
#         #--------------------JSON
#         #json.dump(employee, file, indent=4)#tak zapisujemy w formacie json(co, do czego), indent ladniej wyglada
#         #---------------------CSV
#         writer = csv.writer(file)#przy writerze dawac newline=""
#         for row in employees:
#             writer.writerow(row)
#         print("Text file was created")
# except FileExistsError:
#     print("That file already exists!")

# import json
# import csv

# file_path = "test.txt"
# try:
#     with open(file_path, "r") as file:
#         #----------------JSON
#         #content = json.load(file) to w przypadku json plikow
#         #----------------CSV
#         #content = csv.reader(file)
#         # for line in content:
#         #     print(line)
#         content = file.read()
#         print(content)#json content["name"]
# except FileNotFoundError:
#     print("That file was not found")


# ===========================================PyQt5 wprowadzenie===========================================
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.setGeometry(1000, 500, 500, 500)#wielkosc okna oraz rozmieszczenie
        self.setWindowIcon(QIcon("logo_d.png"))#Ikona apki
        self.button = QPushButton("Click me!", self)
        self.label = QLabel("Hello", self)
        self.initUI()
        ##Zdjecie label
        # label = QLabel(self)
        # label.setGeometry(0, 0, 250, 250)

        # pixmap = QPixmap("projects-bg.png")

        # label.setPixmap(pixmap)

        # label.setScaledContents(True)

        # label.setGeometry((self.width() - label.width()) // 2, 
        #                   (self.height() - label.height()) // 2, 
        #                   label.width(), 
        #                   label.height())

        ##HEllo label
        # label = QLabel("Hello", self)
        # label.setFont(QFont("Arial", 50))
        # label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: #ca03fc;"
        #                     "background-color: #b6b8b6;"
        #                     "font-weight: bold;"
        #                     "font-style: italic;")
        # #label.setAlignment(Qt.AlignTop) #Pionowo w gore
        # # label.setAlignment(Qt.AlignVCenter) #Pionowo center
        # # label.setAlignment(Qt.AlignHCenter) #H-horizontal-poziomo center
        # # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)# CENTER & BOTTOM
        # label.setAlignment(Qt.AlignCenter) # Center & Center
        # # CHECKBOX =======================================

        # self.checkbox= QCheckBox("Do you like food?", self)

        # # RADIO BUTTONS=================================

        # self.radio1 = QRadioButton("Visa", self)
        # self.radio2 = QRadioButton("Mastercard", self)
        # self.radio3 = QRadioButton("Gift Card", self)
        # self.radio4 = QRadioButton("In-Store", self)
        # self.radio5 = QRadioButton("Online", self)
        # self.button_group1 = QButtonGroup(self)
        # self.button_group2 = QButtonGroup(self)

        # # LINE EDIT ====================================

        # self.line_edit = QLineEdit(self)

        # self.button = QPushButton("Submit", self)

    def initUI(self):
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)

        # label1 = QLabel("#1",self)
        # label2 = QLabel("#2",self)
        # label3 = QLabel("#3",self)
        # label4 = QLabel("#4",self)
        # label5 = QLabel("#5",self)

        # label1.setStyleSheet("background-color: red;")
        # label2.setStyleSheet("background-color: green;")
        # label3.setStyleSheet("background-color: blue;")
        # label4.setStyleSheet("background-color: yellow;")
        # label5.setStyleSheet("background-color: purple;")

        # #hbox = QHBoxLayout()#Vbox- pionowo, Hbox-poziomo

        # grid = QGridLayout()

        # grid.addWidget(label1, 0, 0)
        # grid.addWidget(label2, 0, 1)
        # grid.addWidget(label3, 1, 0)
        # grid.addWidget(label4, 1, 1)
        # grid.addWidget(label5, 2, 1)

        # central_widget.setLayout(grid)

        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)# polaczenie funckji z buttonem

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 20px;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        #Stylownianie tak jakby css 
        # self.setStyleSheet("""
        #     QPushButton{
        #         font-size: 40px;
        #         font-family: Arial;
        #         padding: 15px 75px;
        #         margin: 25px;
        #         border: 3px solid;
        #         border-radius: 15px;
        #     }
        #     QPushButton#button1{
        #         background-color: red;
        #     }
        #     QPushButton#button2{
        #         background-color: yellow;
        #     }
        #     QPushButton#button3{
        #         background-color: purple;
        #     }
        #     QPushButton#button1:hover{
        #         background-color: purple;
        #     }
        #     QPushButton#button2:hover{
        #         background-color: red;
        #     }
        #     QPushButton#button3:hover{
        #         background-color: yellow;
        #     }
        # """)

        # # EDIT LINE===========================================
        # self.line_edit.setGeometry(10, 10, 200, 40)
        # self.button.setGeometry(210, 10, 100, 40)

        # self.line_edit.setStyleSheet("font-size: 25px;"
        #                              "font-famili: Arial;")
        # self.line_edit.setStyleSheet("font-size: 25px;"
        #                              "font-famili: Arial;")
        
        # self.button.clicked.connect(self.submit)

        # self.line_edit.setPlaceholderText("Enter your name")

        # # RADIO BUTTON===========================================
        
        # self.radio1.setGeometry(0, 0, 300, 50)
        # self.radio2.setGeometry(0, 50, 300, 50)
        # self.radio3.setGeometry(0, 100, 300, 50)
        # self.radio4.setGeometry(0, 150, 300, 50)
        # self.radio5.setGeometry(0, 200, 300, 50)

        # self.setStyleSheet("QRadioButton{"
        #                    "font-size: 40px;"
        #                    "font-family: Arial;"
        #                    "padding: 10px"
        #                    "}")
        # self.button_group1.addButton(self.radio1)
        # self.button_group1.addButton(self.radio2)
        # self.button_group1.addButton(self.radio3)

        # self.button_group2.addButton(self.radio4)
        # self.button_group2.addButton(self.radio5)

        # self.radio1.toggled.connect(self.radio_button_changed)
        # self.radio2.toggled.connect(self.radio_button_changed)
        # self.radio3.toggled.connect(self.radio_button_changed)
        # self.radio4.toggled.connect(self.radio_button_changed)
        # self.radio5.toggled.connect(self.radio_button_changed)

        # # CHECKBOX===========================================

        # self.checkbox.setGeometry(10, 5, 500, 100)
        # self.checkbox.setStyleSheet("font-size: 30px;"
        #                             "font-family: Arial;")
        # self.checkbox.setChecked(False)
        # self.checkbox.stateChanged.connect(self.checkbox_changed)

    def on_click(self):
        self.button.setText("Clicked!")
        self.label.setText("Goodybye :()")

    def submit(self):
        text = self.line_edit.text()#Zwraca text z lini edit jak wczesnije z radio
        print(f"Hello {text}")
    
    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You dont like food")
    
    def radio_button_changed(self):
        radio_button = self.sender()#Daje info ktory radio wybrano

        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


def main():
    app = QApplication(sys.argv)#pozwala przetwarzac polecenia z terminala czyli arg po wywolaniu zadania
    window = MainWindow()

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



