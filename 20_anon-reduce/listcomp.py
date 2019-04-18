'''
Team Directive - Thomas Zhao & Stefan Tan
SoftDev2 pd8
K#20: Reductio ad Absurdum
2019-04-17
'''

from functools import reduce

file = open("iliad.txt", "rU")
text = file.read()
#print(text)
stripped = text.replace("," , "").replace(".", "").replace(";", "").replace(":", "").replace("!", "").replace('"', "").replace("(", "").replace(")", "").replace("?", "").replace("\n", " ").replace("--", " ")
splitted = stripped.split(" ")

def wordfrequency(word):
    '''RETURNS THE FREQUENCY OF THE GIVEN WORD IN INPUT FILE'''
    list = [1 for x in splitted if x == word]
    num = reduce(lambda a, b: a + b, list)
    return num

def groupfrequency(group):
    '''RETURNS THE COLLECTIVE FREQUENCIES OF THE WORDS IN THE LIST GROUP'''
    list = [1 for x in splitted if x in group]
    num = reduce(lambda a, b: a + b, list)
    return num

def mostfrequent():
    '''RETURNS THE MOST FREQUENT WORD IN THE INPUT FILE
       NOTE: MAY TAKE SEVERAL MINUTES, DEPENDING ON FILE SIZE'''
    i = 0
    current_king = ('placeholder', 0)
    checked = set()
    for word in splitted:
        i = i + 1
        print(str(i) + " " + word)
        if word not in checked and not word == '':
            num = wordfrequency(word)
            checked.add(word)
            if num > current_king[1]:
                current_king = (word, num)
    return current_king

print(wordfrequency('can'))
print(groupfrequency(['can', 'have']))
print(mostfrequent())
# this last one took 5.5 minutes for me
'''
('the', 13386)
real    5m35.832s
user    4m0.469s
sys     0m11.188s
''' 
