# playing with variables and str method along with concatenation/interpolation
# age = 5
# seconds_in_day = 24 * 60 ** 2
# days_in_year = 365
# print('seconds_in_day: ', seconds_in_day, 'days_in_year: ', days_in_year, 'age in years: ', age)
# print('A five year old has lived ' + str(age * seconds_in_day * days_in_year) + ' seconds')

# # Getting user input and doing something with it.
# entered_age = input('Enter your age: ')
# print('User entered an age of: ' + entered_age)
# print('The User has lived at least ' + str(int(entered_age) * seconds_in_day * days_in_year) + ' seconds')

# # Format
# print('The User has lived at least {} seconds.'.format(str(int(entered_age) * 365 * 24 * 60 ** 2)))
# print('The User has lived at least {} seconds.'.format(int(entered_age) * 365 * 24 * 60 ** 2))
# print('The User has lived at least {} seconds. This corresponds to {} years'.format(int(entered_age) * 365 * 24 * 60 ** 2, entered_age))
# test = 'testicles'
# intro = 'Hello, I\'m here to talk about {try_this}'
# print(intro.format(try_this=test))
# print("{monster} has now eaten {city}".format(city='Tokyo', monster='Mothra'))
# print("We have {0} hectares planted to {1}.".format(49, "okra"))
# print("The {structure} sank {1} times in {0} years.".format(3, 2, structure='castle'))

# Lists
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers) # => 10
# print(numbers[9])
# print(numbers[len(numbers)-1])
# for number in numbers:
#   print(number)

# print('power of Two:')
# for number in numbers: 
#   print(number ** 2)


#boolean
# greater_than_three = 5 > 3 # => True
# equal_to_five = 5 == 5

# print(greater_than_three, equal_to_five)
# for thing in numbers: 
#   print('Is {0} greater than 5? '.format(thing), thing > 5)

# for thing in numbers: 
#   if thing > 5:
#    print('{0} is greater than 5'.format(thing))
#   else:
#    print('{0} is less than 5'.format(thing))

# magic_numbers = [3, 9]
# user_number = input('pick a number!!! ')
# if int(user_number) in magic_numbers:
#   print('you picked a magic number!')
# else:
#   print('nope, you didn\'t get it right')

# chances = 3

# for i in range(chances): # rante(chances) is [0, 1, 2]
#   user_selection = input('Please guess the magic number: ')
#   if user_selection == '':
#     user_selection = input('Please enter a valid number!  ')
#   if int(user_selection) in magic_numbers:
#     print('{0} is a magic number!'.format(user_selection))
#     break
#   else: 
#     print('{0} is not a magic number, you have {1} chance(s) left'.format(user_selection, chances - 1))

# Generating random numbers in Python
import random # this imports the random library and it's child methods
# total_rando = random.randint(0, 9) #must specify range
# print('Look at this random number {rando}'.format(rando = total_rando))

# random_numbers = []
# for i in range(10):
#   random_numbers.append(random.randint(0, 9))
# print('Look at this randos!', random_numbers)
# random_numbers.sort()
# print(random_numbers)
# lowest_number = str(random_numbers.pop(0))
# print('The lowest rando there is: {lowest}'.format(lowest = lowest_number))

# minimum = 100
# random_numbers = []
# for index in range(10):
#   random_number = random.randint(0, 100)
#   random_numbers.append(random_number)
#   if random_number <= minimum:
#     minimum = random_number
# print('Of the numbers in the list: {0}, the lowest number is {1}'.format(random_numbers, minimum))

def ask_user_and_check_number(list):
  user_number = int(input('Enter a number betwixt 0 and 9: '))
  if user_number in list:
    print('You chose a magic number!')
  else: 
    print('The number you chose is not a magic number :(')

magic_numbers = [random.randint(0, 9), random.randint(0,9)]
# chances = 3
# for attempt in range(chances): # range(chances) equates to [0, 1, 2]
#   print('This is attempt {}'.format(attempt + 1))
#   ask_user_and_check_number(magic_numbers)

def run_program_x_times(x, list):
  for attempt in range(x): # range(chances) equates to [0, 1, 2]
    print('This is attempt {}'.format(attempt + 1))
    ask_user_and_check_number(list)

run_program_x_times(4, magic_numbers)






























