# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List, Dict, Tuple
a = 1
b = "1"
c = 1.5
d = True
f = [1, 2, 3,]
g = (1, 2, 3)
h = 1, 2, 3
i = {1, 2, 3}
j = {"a": 1, "b": 2}
k, l, m = 1, 2, 3

print("hello world")

class A:
    __a: int #private
    _b: str # protected
    c: bool #public
    
    def __init__(self, a: int = 1, b: str = "a"):
        self.__a = a
        self._b = "a"
        
    def print_and_get_a(self) -> str:
        print(self.__a)
        return self.__a
 
    
    @staticmethod
    def a():
        print("a")
        
    @classmethod
    def b(cls):
        cls.a()
    
        
a: A = A(5, b="a")
a.print_and_get_a()

for i in range(1, 10, 2):
    print(i)
    

l: List[int] = [1, 2, 3]

for i in l:
    print(i)
    
print(l[0])


    
    
        