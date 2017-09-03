import random

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]

def ask_user_and_check_number(list):
  user_number = int(input('Enter a number between 0 and 9: '))
  if user_number in list: 
    return 'The number {} is a magic number!'.format(user_number)
  return 'The number {} is a basic bitch'.format(user_number)

def run_program_x_times(x, list):
  for attempt in range(x): # range(chances) is [0, 1, 2]
    print('This is attempt {}'.format(attempt + 1))
    print(ask_user_and_check_number(list))

user_attempts = int(input('Enter the number of attempts: '))

run_program_x_times(user_attempts, magic_numbers)

# my_numbers = [random.randint(0, 10) for x in range(3)]
# print(my_numbers)