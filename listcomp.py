'''
Team Directive - Thomas Zhao & Stefan Tan
SoftDev2 pd8

'''

from functools import reduce

file = open("iliad.txt", "rU")

text = file.read().strip("\n").strip('').split(" ")

for word in text:
    word.strip("\n")

def wordfreq(w):
    return reduce((lambda x,y : x + 1), text) 
    
#print(text)
print(wordfreq("can"))
