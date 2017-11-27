should_continue = True
if should_continue:
	print("It is currently True");

known_peeps = ["John", "Anna", "Mary"]
person = input('Enter the person you know: ')

is_there = False

# for name in known_peeps:
# 	if person == name:
# 		is_there = True
# if is_there:
# 	print('Yeah! {} is here!'.format(person))
# else:
# 	print('Nope {} hasn\'t been here all night!'.format(person))
#
if person in known_peeps:
	print('Yeah! {} is here!'.format(person))
else:
	print('Nope {} hasn\'t been here all night!'.format(person))


# Exercise

def who_do_you_know():
	known_people = input("Enter the people you know separated by a comma! ")
	peeps = [person.strip() for person in known_people.split(',')]
	return peeps

def ask_user(name_list):
	user_choice = input("Please enter a name: ")
	if user_choice in name_list:
		print('Hey hey it looks like you know {}'.format(user_choice))

user_list_of_known_people = who_do_you_know()

ask_user(user_list_of_known_people)
