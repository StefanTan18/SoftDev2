'''
Stefan Tan
SoftDev2 pd8
K22 -- Closure
2019-04-30
'''

def repeat(s):
    def num_repeats(n):
        return s * n
    return num_repeats

r1 = repeat("hello")
print(r1(2)) #Expected Result: hellohello
r2 = repeat("goodbye")
print(r2(2)) #Expected Result: goodbyegoodbye
print(repeat('cool')(3)) #Expected Result: coolcoolcool


def make_counter():
    x = 0
    def count():
        nonlocal x
        x += 1
        return x
    def get_count():
        return x
    return count, get_count

ctr1, accessor1 = make_counter()
print(ctr1()) #Expected Result: 1
print(ctr1()) #Expected Result: 2
ctr2, accessor2 = make_counter()
print(ctr2()) #Expected Result: 1
print(ctr1()) #Expected Result: 3
print(ctr2()) #Expected Result: 2

print(accessor1()) #Expected Result: 3
print(accessor2()) #Expected Result: 2

'''
def adder(a, b):
    return a + b

def caller(c):
    print(c(2,4))
    print(c(3,5))

caller(adder)
'''

'''
def outer(x):
    def contains(l):
        return x in l
    return contains

contains_15 = outer(15)
print(contains_15([1,2,3,4,5]))
print(contains_15([13, 14, 15, 16, 17]))
print(contains_15(range(1,20)))

print(outer(42))
del outer
#outer(42)

print(contains_15(range(14,20)))
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




