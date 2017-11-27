
grades = [77, 80, 90, 95, 100]  # this is a list, known as an array in JS

tuple_grades = (77, 80, 90, 95, 100)

set_grades = {77, 80, 90, 95, 100}  # unique and unordered
set_grades2 = {77, 80, 90, 95, 100, 100}
# lists work in almost the same exact manner as arrays in JS
# Tuples are immutable, meaning they cannot be changed!
# (continued...)Meaning you cannot add/append to the tuple like you can with lit.
# Sets do not guarantee order! Also, every value in a set is unique, meaning dupe values will result in only one.

print(set_grades)
print(set_grades2)  # prints: {100, 77, 80, 90, 95}

grades.append(62)  # lists have methods (like append) that specifically work with that value type
print(grades)
print(sum(grades) / len(grades))

print('first tuple ---->', tuple_grades)
tuple_grades = tuple_grades + (62,)  # IMPORTANT! Notice the comma, this makes it a single-value tuple
print('modified tuple ---->', tuple_grades)

#  In the example above, the tuple is not being modified because it can't be because it's immutable
#  what happened was tuple_grades was redefined to be the original values concatenated with an added tuple
#  tuples and sets don't support element assignment. Meaning you can't assign position in tuples like tuple[0] = 'blah'

set_grades.add(60)  # you can add to a set using the method add
set_grades.add(60)  # this line will be result in no change to set_grades because 60 is already in the set
print(set_grades)


#  Set Operations

lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# print(lottery_numbers.intersection(winning_numbers))  # => {1, 3, 5}
# print(lottery_numbers.union(winning_numbers))  # => {1, 2, 3, 4, 5, 7, 9, 11}
# print(lottery_numbers.difference(winning_numbers))  # => {2, 4}
# print(winning_numbers.difference(lottery_numbers))  # => {9, 11, 7}

