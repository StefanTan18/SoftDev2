import math

def pythtriple(n):
    list = [(x, y, int(math.sqrt(x*x + y*y))) for x in range(1, n) for y in range(x, n) if (math.sqrt(x*x + y*y)).is_integer()]
    print(list)

def quicksort()
pythtriple(10)

