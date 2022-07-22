# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 18:31:42 2022

@author: Kachi
"""
total = 0
number = int(input("Enter a number, enter 0 to calculate sum: "))
while number != 0:
    total += number
    number = int(input("Enter a number, enter 0 to calculate sum: "))
print(f"Sum is {total}")