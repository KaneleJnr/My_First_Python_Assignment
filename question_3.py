# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 18:42:09 2022

@author: Kachi
"""

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Enter the operation [+, -, *, /, mod, pow, div]: ")
if operation == "+":
    ans = num1 + num2
elif operation == "-":
    ans = num1 - num2
elif operation == "*":
    ans = num1 * num2
elif operation == "/":
    ans = num1 - num2
elif operation == "mod":
    ans = num1 % num2
elif operation == "pow":
    ans = num1 ** num2
elif operation == "div":
    ans = num1 // num2
print(f"{num1} {operation} {num2} = {ans}")