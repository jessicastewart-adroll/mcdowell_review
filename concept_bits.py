#!/bin/python3

import sys

def lonely_integer(a):
    unique = 0
    for num in a:
        unique ^= num
    return unique 

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

###

a = [10, 10, 11, 12, 11]

def lonely_integer(a):
  cache = {}
  for num in a:
    if not cache.get(num):
      cache[num] = 1
    else: 
      cache[num] += 1
      
  for num in a:
    if cache[num] < 2:
      return num
  
print(lonely_integer(a))
