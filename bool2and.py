"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""
bool_one = 3 < 2 and 100 > 5000 #False
print bool_one

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5 #False
print bool_two

bool_three = 19 % 4 != 300 / 10 / 10 and -1 < -55 #False
print bool_three

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2 #True
print bool_four

bool_five = 10**2 == 100 and 10 == 100**0.5 #True
print bool_five