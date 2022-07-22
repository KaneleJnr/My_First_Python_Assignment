# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:17:29 2022

@author: Kachi
"""

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
LNo = n3
n = [n1, n2, n3]
if n1 < n2 < n3:
    LNo = n2
else:
    if n2 < n1 < n3:
        LNo = n1
    else:
        if n1 < n3 < n2:
            LNo = n3

print(max(n))
print(min(n))
print(LNo)    