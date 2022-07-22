# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 19:23:11 2022

@author: Kachi
"""

# I'd do this one with dictionaries
my_string = input("Enter the string you want to encode: ")
encode_dic = {}
for i in my_string:
    if i in encode_dic:
        encode_dic[i] += 1
    else:
        encode_dic[i] = 1
encode_string = ""
for i in encode_dic:
    encode_string += (i + str(encode_dic[i]))
print(encode_string)