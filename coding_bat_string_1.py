# Given an "out" string length 4, such as "<<>>", and a word, return a new string
# where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
    new_word = (out[0:2] + word + out[2:4])
    return new_word


# Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
# The string length will be at least 2.

def extra_end(st):
    x= (st[-2]+st[-1])*3
    return x


# Given a string, return the string made of its first two chars, so the String "Hello" yields
# "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X",
# and the empty string "" yields the empty string "".

def first_two(st):
    if 0<len(st)<2:
        return st
    elif len(st)==0:
        return ""
    else:
        return st[0:2]


# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(st):
    x = len(st) // 2
    return st[:x]


# Given a string, return a version without the first and last char,
# so "Hello" yields "ell". The string length will be at least 2.


def without_end(st):
    st=st [1:-1]
    return st


# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).

def combo_string(a, b):
    return str(b+a+b) if len (a)> len(b) else str(a+b+a)


# Given 2 strings, return their concatenation,
# except omit the first char of each. The strings will be at least length 1.


def non_start(a, b):
    if len(a)>0 and len(b)>0:
        return (a[1:]+b[1:])



# Given a string, return a "rotated left 2" version where
# the first 2 chars are moved to the end. The string length will be at least 2.

def left2(st):
    if len(st) >= 2:
        return st[2:] + st[:2]
