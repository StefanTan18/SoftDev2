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
    print'yum'
    
loop1()
listcomp1()
loop2()
listcomp2()
loop3()
listcomp3()
loop4()
