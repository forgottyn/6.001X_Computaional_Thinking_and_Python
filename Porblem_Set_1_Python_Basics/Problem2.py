#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
num = 0
count = 0
for i in range(len(s)):
    if s[i:].startswith('bob'):
        num += 1
print("Number of times bob occurs is: ", num)

