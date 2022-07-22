# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:04:21 2022

@author: Kachi
"""

n = int(input("Enter the number of elements: "))
count = 0

for i in range(1, n+1):
    if count >= n: break
    for j in range(i):
        if count < n:
            print(i, end = " ")
            count += 1
        else: break