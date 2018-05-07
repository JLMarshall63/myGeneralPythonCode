'''
Boolean operators aren't just evaluated from left to right.
Just like with arithmetic operators, there's an order of operations
for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.

For example, True or not False and False returns True.
Parentheses () ensure your expressions are evaluated in the
order you want. Anything in parentheses is evaluated as its
own unit.

Assign True or False as appropriate for bool_one through bool_five.

Set bool_one equal to the result of False or not True and True
Set bool_two equal to the result of False and not True or True
Set bool_three equal to the result of True and not (False or False)
Set bool_four equal to the result of not not True or False and not True
Set bool_five equal to the result of False or not (True and True)

'''
bool_one = 2 < 1 or not 2 > 1 and 3 > 2

bool_two = 1 > 12 and not 2 > 4 or 4 > 2

bool_three = 6 > 4 and not (4 < 3 or 3 < 2)

bool_four = not not 4 > 3 or 2 > 3 and not 5 > 6

bool_five = 7 < 1 or not (9 > 1 and 8 > 1)