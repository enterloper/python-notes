import random


def menu():
    # Ask player for numbers
    user_numbers = get_x_player_numbers(6)
    # Calculate lottery numbers
    lotto_numbers = create_x_lottery_numbers(6)
    # print out the winnings
    matching_numbers = user_numbers.intersection(lotto_numbers)
    number_of_matches = len(matching_numbers)
    print('You matched {0}. You won ${1}!'.format(matching_numbers, 100 ** number_of_matches))


# User can pick 6 numbers
def get_x_player_numbers(x):
    number_csv = input('Please enter {} numbers separated by commas: '.format(x))
    # Now, I want to create a set of integers from this number_csv
    split_numbers = number_csv.split(',')
    return {int(number) for number in split_numbers}


# Lottery calculates x random numbers (between 1 and 20)
def create_x_lottery_numbers(x):
    lotto_numbers = set()
    while len(lotto_numbers) < 6:
        lotto_numbers.add(random.randint(1, 20))
    return lotto_numbers

menu()