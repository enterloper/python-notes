my_variable = "yoda"

# print(my_variable[0])  # => y  But... this sucks.

for character in my_variable:
	print(character)

my_list = [1, 3, 5, 7, 9]

for number in my_list:
	print(number ** 2)


count = 0
while count < 10:
	count = count + 1
	print(count)

user_wants_number = True

while user_wants_number:
	user_input = input("Do you want a number? (y/n) ".lower())
	if user_input == 'y':
		print('You get a {}, just like the last guy!'.format(10))
	if user_input == 'n':
		user_wants_number = False

