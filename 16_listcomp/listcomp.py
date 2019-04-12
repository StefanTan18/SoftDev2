'''
Stefan Tan
SoftDev2 pd8
K16 -- Do You Even List?
2019-04-11
'''

UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMS = "1234567890"
SPEC_CHAR = ".?!&#,;:-_*"

def valid_pwd(pwd):
    pwd_check = [1 if x in UC_LETTERS else 2 if x in LC_LETTERS else 3 if x in NUMS else 0 for x in pwd]
    #print(pwd_check)
    if (1 in pwd_check and 2 in pwd_check and 3 in pwd_check):
        return True
    return False

def pwd_rating(pwd):
    str_rating = 0
    pwd_check = [1 if x in UC_LETTERS else 2 if x in LC_LETTERS else 3 if x in NUMS else 4 if x in SPEC_CHAR else 0 for x in pwd]
    #print(pwd_check)
    num_uc = pwd_check.count(1);
    num_lc = pwd_check.count(2);
    num_nums = pwd_check.count(3);
    num_char = pwd_check.count(4);

    if (num_uc > 3):
        str_rating += num_uc
    if (num_lc > 3):
        str_rating += num_lc
    if (num_nums > 1):
        str_rating += num_nums
    if (num_char > 1):
        str_rating += num_char

    if str_rating > 10:
        str_rating = 10

    return str_rating
    
print(valid_pwd("123456"))
print(valid_pwd("1as456"))
print(valid_pwd("Das456"))

print(pwd_rating("Das456"))
print(pwd_rating("WIFIda291"))
print(pwd_rating("U+RkbiWn!)WT6Pg"))
