import random
import os
import time
from getkey import getkey, key

monkey_i = random.randint(1,18)
monkey_j = random.randint(1,18)
fruits_i = random.randint(1,18)
fruits_j = random.randint(1,18)

monkey = "🐒"
closeays_monkey = "🙈"
fruits = "🍌🍍🍒🍓🍊🍉"
fruit = random.choice(fruits)
hearts = "❤❤❤"
score = 0

while True:
    if score >= 3:
        monkey = "🐵"
    os.system('cls')
    print(f'You louse -> you have {hearts}   hearts')
    print(f"Monkey score = {score}")
    for i in range(20):
        for j in range(20):
            if i == 0 or i == 19:
                print("-", end = " ")
            elif j == 0 or j == 19:
                print("|", end = " ")
            elif i == monkey_i and j == monkey_j:
                print(monkey, end = "")
            elif i == fruits_i and j == fruits_j:
                print(fruit, end = "")
            else:
                print(".", end = " ")
        print()
    cord = getkey()
    cord = cord.upper()
    if cord == "W":
        monkey_i -= 1
    elif cord == "S":
        monkey_i += 1
    elif cord == "A":
        monkey_j -= 1
    elif cord == "D":
        monkey_j += 1
    if monkey_i == fruits_i and monkey_j == fruits_j:
        score += 1
        fruits_i = random.randint(1,18)
        fruits_j = random.randint(1,18)
        fruit = random.choice(fruits)
    if monkey_i == 0 or monkey_i == 19 or monkey_j == 0 or monkey_j == 19:
        hearts = hearts[:-1]
        score = 0
        monkey = "🐒"
        monkey_i = random.randint(1,18)
        monkey_j = random.randint(1,18)
        fruits_i = random.randint(1,18)
        fruits_j = random.randint(1,18)
        time.sleep(0.02)
        print(f'You louse -> you have 0 hearts')
    if hearts == '':
        print(f"{closeays_monkey}---------- GAME OVER ----------")
        break