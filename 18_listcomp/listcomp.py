'''
Team Directive - Thomas Zhao & Stefan Tan
SoftDev2 pd8
K18 -- Getting Clever with List Comprehensions
2019-04-15
'''

import math

def pythtriple(n):
    list = [(x, y, int(math.sqrt(x*x + y*y))) for x in range(1, n) for y in range(x, n) if (math.sqrt(x*x + y*y)).is_integer()]
    print(list)

unsorted = [6, 4, 8, 5, 1, 7, 9, 2, 3] 

def quicksort(list):
    if len(list) < 2:
        return list
    pivot = list[0]
    l = quicksort([x for x in list[1:] if x < pivot])
    g = quicksort([x for x in list[1:] if x >= pivot])
    return l + [pivot] + g
    
pythtriple(10)
print(quicksort(unsorted))
