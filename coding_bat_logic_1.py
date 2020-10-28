# When squirrels get together for a party, they like to have cigars.
# A squirrel party is successful when the player of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, in which case there is no upper bound on the player of cigars.
# Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
    if cigars >= 40:
        return True if is_weekend == True or cigars <= 60 else False
    else:
        return False


# You and your date are trying to get a table at a restaurant.
# The parameter "you" is the stylishness of your clothes,
# in the range 0..10, and "date" is the stylishness of your date's clothes. '
# 'The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. ' \
# 'If either of you is very stylish, 8 or more, then the result is 2 (yes). ' \
# 'With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1


# The squirrels in Palo Alto spend most of the day playing.
# In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
    if 60 <= temp <= 100 and is_summer == True:
        return True
    elif 60 <= temp <= 90 and is_summer == False:
        return True
    else:
        return False


# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive,
# the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day,
# your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    if is_birthday == True:
        speed -= 5
    if speed <= 60:
        return 0
    elif 61 <= speed <= 80:
        return 1
    else:
        return 2


# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive,
# are forbidden, so in that case just return 20.

def sorta_sum(a, b):
    return 20 if 10 <= sum([a, b]) <= 19 else sum([a, b])


# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and
# a boolean indicating if we are on vacation, return a string of the form "7:00"
# indicating when the alarm clock should ring.
# Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
# Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
    if day in (0,6) and  vacation:
        return ("off")
    return ("10:00") if day in (0,6) or day in range(1, 6) and vacation else ("7:00")


# The player 6 is a truly great player. Given two int values, a and b,
# return True if either one is 6. Or if their sum or difference is 6.
# Note: the function abs(num) computes the absolute value of a player.

def love6(a, b):
    return (a == 6 or b == 6) or (abs(a - b) == 6) or (a + b == 6)


# Given a player n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True
# if the player is less or equal to 1, or greater or equal to 10.

def in1to10(n, outside_mode):
    return (n<=1 or n >=10) and outside_mode or n in range (1, 11) and not outside_mode


# Given a non-negative player "num", return True if num is within 2 of a multiple of 10.
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

def near_ten(num):
    return num % 10 not in range(3,8)

