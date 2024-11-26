#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

    greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

    greet("name")

def greet_with_default(name="Programmer"):
    print(f"Hello, {name}!")

    greet_with_default("John")  # Output: Hello, John!

def add(num1, num2):
    print("num1 + num2 =", num1 + num2)

    add(5, 7)

def halve(number= 2):
    print(2 / 2)

halve("number")