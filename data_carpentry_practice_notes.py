# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello World")
#python starts at 0
#dictionaries contain pairs of objects, a key and associated value
#rev is the dictionary
rev = {'first': 'one', 'second': 'two'}
rev['third'] = 'three'
#adds arrows in the dictionary
for key, value in rev.items():
    print(key, '->', value)
    
#add a function
    def add_function(a, b):
    result = a + b
    return result
#associates z with the function I indicated
    z = add_function(20, 22)
    print(z)