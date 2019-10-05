# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
array = np.array([1, 2, 3], dtype=np.bool)


from typing import List, Dict, Tuple

if 1 == 2 :
    print("?")
elif 2 == 3:
    print("?" * 20)
else:
    print ("-" * 30)
    
left: List[int] = [1, 2, 3]
right: List[str] = ["ala", "ma", "kota"]
print(left + right)


some_numbers: List[int] = []
for i in left:
    some_numbers.append(i + 1)
    
print(some_numbers)

class A:
    __a: str
    def __init__(self, a: str = "A"):
        self.__a = a
        
l: List[A] = [A()] * 20



generator = (i + 1 for i in range(11) if i % 2 == 0)

try:
    while True:
        print(next(generator))
except StopIteration:
    pass

print(dir(generator))
generator.close()

def f():
    raise NotImplementedError()
    
try:
    f()
except NotImplementedError:
    print("Not implemented error")
except:
    print()
    
    
    
with open("file.txt", "r") as f:
    print(f.read())
    
f = open("file.txt", "r")

print