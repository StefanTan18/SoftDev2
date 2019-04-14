'''
Team Directive - Thomas Zhao & Stefan Tan
SoftDev2 pd8
K17 -- PPFTLCW
2019-04-12
'''

def loop1():
    list = []
    for x in range(5):
        list.append(str(x*2)+str(x*2))
    print(list)

def listcomp1():
    list = [str(x*2)+str(x*2) for x in range(5)]
    print(list)

def loop2():
    list = []
    for x in range(5):
        list.append(10*x + 7)
    print(list)

def listcomp2():
    list = [10*x+7 for x in range(5)]
    print(list)

def loop3():
    list = []
    index1 = 0
    index2 = 0
    for x in range(3):
        list.append(0)
        list.append(index1)
        list.append(index2)
        index1 = index1 + 1
        index2 = index2 + 2
    print(list)

def listcomp3():
    list = [ x * y for x in range(3) for y in range(3)]
    print(list)

def loop4():
    list = []
    for x in range(101):
        primes = [0,2,3,5,7]
        if (x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0) and x not in primes:
            list.append(x)
    print(list)

def listcomp4():
    primes = [0,2,3,5,7]
    list = [x for x in range(101) if (x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0) and x not in primes] 
    print(list)

def loop5():
    list = []
    for x in range(2, 101):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            list.append(x)
    print(list)

def listcomp5():
    list = [x for x in range(2, 101) if 0 not in [x % y for y in range(2,x)]]
    print(list)

def loop6(n):
    list = []
    for x in range(1, n+1):
        if n % x == 0:
            list.append(x)
    print(list)

def listcomp6(n):
    list = [x for x in range(1, n+1) if n % x == 0]
    print(list)

m = [[1,2],[3,4],[5,6]] 
    
def loop7(m):
    list = []
    row = []
    for c in range(len(m[0])):
        for r in range(len(m)):
            row.append(m[r][c])
        list.append(row)
        row = []
    print(list)

def listcomp7(m):
    list = [[m[r][c] for r in range(len(m))] for c in range(len(m[0]))] 
    print(list)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Expected Result:")
print("['00', '22', '44', '66', '88']\n")
print("Testing loop method...")
loop1()
print("Testing list comprehension method...")
listcomp1()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Expected Result:")
print("[7, 17, 27, 37, 47]\n")
print("Testing loop method...")
loop2()
print("Testing list comprehension method...")
listcomp2()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Expected Result:")
print("[0, 0, 0, 0, 1, 2, 0, 2, 4]\n")
print("Testing loop method...")
loop3()
print("Testing list comprehension method...")
listcomp3()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Expected Result:")
print("[4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]\n")
print("Testing loop method...")
loop4()
print("Testing list comprehension method...")
listcomp4()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Expected Result:")
print("[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n")
print("Testing loop method...")
loop5()
print("Testing list comprehension method...")
listcomp5()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Expected Result:")
print("[1, 2, 3, 4, 6, 12]\n")
print("Testing loop method...")
loop6(12)
print("Testing list comprehension method...")
listcomp6(12)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Original Matrix:")
print("[[1, 2], [3, 4], [5, 6]]")
print("Expected Result:")
print("[[1, 3, 5], [2, 4, 6]]\n")
print("Testing loop method...")
loop7(m)
print("Testing list comprehension method...")
listcomp7(m)
