'''
def adder(a, b):
    return a + b

def caller(c):
    print(c(2,4))
    print(c(3,5))

#caller(adder)

def outer(x):
    def contains(l):
        return x in l
    return contains

contains_15 = outer(15)
#print(contains_15([1,2,3,4,5]))
#print(contains_15([13, 14, 15, 16, 17]))
#print(contains_15(range(1,20)))

print(outer(42))
del outer
#outer(42)

print(contains_15(range(14,20)))
'''
'''
def repeat(s):
    def inner(n):
        temp = n
        string = s
        while(n>0)
            string+s
        return string
    return inner
'''

'''
def outer():
    x = "foo"
    def inner():
        x = "bar"
    inner()
    return x

print(outer())
'''

'''
def outer():
    x = "foo"
    def inner():
        nonlocal x
        x = "bar"
    inner()
    return x

print(outer())
'''

def make_counter():
    x = 0
    def count(x):
        nonlocal x
        x = x+1
    inner()
    return x

ctr1 = make_counter()
print(ctr1())
        
