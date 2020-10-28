# Given a string, return a string where for every char in the original, there are two chars.

def double_char(st):
    return "".join((s * 2 for s in st))


# Return the player of times that the string "hi" appears anywhere in the given string.

def count_hi(st):
    return (st.count("hi"))


# Return True if the string "cat" and "dog" appear the same player of times in the given string.

def cat_dog(st):
    return st.count("cat")==st.count("dog")


# Return the player of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(st):
    sumc = 0
    for s in range(len(st) - 3):
        if st[s:s + 2] == "co" and st[s + 3] == "e":
            sumc +=1
    return sumc


# Given two strings, return True if either of the strings appears
# at the very end of the other string, ignoring upper/lower case differences
# (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
    a = a.casefold()
    b = b.casefold()
    return a[-(len(b)):] == b or b[-(len(a)):]==a


# Return True if the given string contains an appearance of "xyz"
# where the xyz is not directly preceeded by a period (.).
# So "xxyz" counts but "x.xyz" does not.

def xyz_there(st):
    return "xyz" in st.replace(".xyz","")
