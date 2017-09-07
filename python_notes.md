#Numbers and Strings

Strings 
'2' * 3 will equate to '222'
'2' + '2' will equate to '22'
2 + '2' will throw a TypeError: Can't convert 'int' object to str implicitly


#Variables
how to declare a variable:
x = 5

how to reference x
x # => 5
x + 5 # => 10

#converting numbers to strings with str()
  age = 34
  age // => 34
  age_string = str(age)
  age_string // => '34'
  age // => 34

  age_string + ' years' # => '34 years'

  str(age) + ' years' # => '34 years'

#converting strings to numbers with int() and using input
  entered_age = input('Enter your age: ')
  print('User entered an age of: ' + entered_age)
  print('The User has lived at least ' + str(int(entered_age) * seconds_in_day * days_in_year) + ' seconds')


#format
  print('The User has lived at least {} seconds.'.format(str(int(entered_age) * 365 * 24 * 60 ** 2)))
  print('The User has lived at least {} seconds.'.format(int(entered_age) * 365 * 24 * 60 ** 2))
  print('The User has lived at least {} seconds. This corresponds to {} years'.format(int(entered_age) * 365 * 24 * 60 ** 2, entered_age))
  ## This is a more readable approach.

  #see here: https://infohost.nmt.edu/tcc/help/pubs/python/web/new-str-format.html
  test = 'testicles'
  intro = 'Hello, I\'m here to talk about {try_this}'
  print(intro.format(try_this=test))
  print("{monster} has now eaten {city}".format(city='Tokyo', monster='Mothra'))
  print("We have {0} hectares planted to {1}.".format(49, "okra"))
  print("The {structure} sank {1} times in {0} years.".format(3, 2, structure='castle'))

#Lists
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers) # => 10
print(numbers[9])
print(numbers[len(numbers)-1])
for number in numbers:
  print(number)

print('power of Two:')
for number in numbers: 
  print(number ** 2)

#boolean
greater_than_three = 5 > 3 # => True
equal_to_five = 5 == 5

print(greater_than_three, equal_to_five) # => True, True

for thing in numbers: 
  print('Is {0} greater than 5? '.format(thing), thing > 5)

for thing in numbers: 
  if thing > 5:
   print('{0} is greater than 5'.format(thing))
  else:
   print('{0} is less than 5'.format(thing))

# the 'in' and 'not' keywords

### not is like a bang in JS

10 in numbers # => False
10 not in numbers # => True

if not 3 > 5:
  print('this is weird')


# for-loops

print(greater_than_three, equal_to_five)
for thing in numbers: 
  print('Is {0} greater than 5? '.format(thing), thing > 5)

for thing in numbers: 
  if thing > 5:
   print('{0} is greater than 5'.format(thing))
  else:
   print('{0} is less than 5'.format(thing))

magic_numbers = [3, 9]
user_number = input('pick a number!!! ')
if int(user_number) in magic_numbers:
  print('you picked a magic number!')
else:
  print('nope, you didn\'t get it right')

chances = 3

for i in range(chances): # rante(chances) is [0, 1, 2]
  user_selection = input('Please guess the magic number: ')
  if user_selection == '':
    user_selection = input('Please enter a valid number!  ')
  if int(user_selection) in magic_numbers:
    print('{0} is a magic number!'.format(user_selection))
    break
  else: 
    print('{0} is not a magic number, you have {1} chance(s) left'.format(user_selection, chances - 1))

# Generating random numbers in Python

# Generating random numbers in Python
import random
total_rando = random.randint(0, 9) #must specify range
print('Look at this random number {rando}'.format(rando = total_rando))

random_numbers = []
for i in range(10):
  random_numbers.append(random.randint(0, 9))
print('Look at this randos!', random_numbers)
random_numbers.sort()
print(random_numbers)
lowest_number = str(random_numbers.pop(0))
print('The lowest rando there is: {lowest}'.format(lowest = lowest_number))

## List comprehension
user_input = '1,2,3,4,5,6'
user_numbers = user_input.split(',') # => [1, 2, 4, 3, 5, 6]
user_numbers_as_int = []
for number in user_numbers: 
  user_numbers_as_int.append(int(number))

[number for number in user_numbers]

user_numbers = ['1','2','3','4','5','6']
user_numbers # => ['1', '2', '3', '4', '5', '6']
user_numbers_as_int = [int(number) for number in user_numbers_as_int]
user_numbers_as_int # => [1, 2, 3, 4, 5, 6]

# Set - a list with unique values only. 
# https://infohost.nmt.edu/tcc/help/pubs/python/web/set-types.html

numbers = set()
numbers # => set()
numbers.add(3)
numbers # notice curly braces  => {3} 
numbers.add(3)
numbers # notice that it only contains the original 3 => {3}

lottery_values = {3, 5, 17, 6}
lottery_values # => {3, 5, 17, 6}
user_values = {3, 5, 11, 2}
user_values # => {3, 5, 11, 2} 
lottery_values.intersection(user_values) # => {3, 5}
user_values.intersection(lottery_values) # => {3, 5}

# Dictionary
sample_dictionary = {'name': 'Rich', 'mark': 70}

print(sample_dictionary['name']) # => 'Rich'

# OOP -> Classes in Python
# Must use dot notation when accessing a class's values.

class Student:
  def __init__(self, name):
    self.name = name
    self.marks = []

  def average_mark(self):
    number = len(self.marks)
    if number == 0:
      return 'The student {} has no marks to average!'.format(self.name)

    total = sum(self.marks)
    return total / number


## in movie.py
class Movie:
  def __init__(self, title, genre):
    self.title = title
    self. genre = genre

## in user.py
class User:
  def __init__(self, name):
    self.name = name
    self.movies = []

  def __repr__(self):
    return "<User {}>".format(self.name)



## Writing to a csv file in Python
# must open a file and close it to insure the file is properly saved.
# 'w' stands for 'write', 'r' stands for 'r'

with open('my_file.txt', 'w') as f: 
  f.write('Hello, World!')
# f.close() is not necessary because we are using a with block

with open('my_file.txt', 'r') as f:
  print(f.readline())    # => 'Hello, World!'


### reading a file from csv
content = f.readlines() # reads multiple lines and returns a list.
content = f.readline

  def load_from_file(self, filename):
    with open('{}.txt'.format(filename), 'r') as f:
      content = f.readlines()
      username = content[0]
      movies = []
      
      #  Start iterating from index 1 to the end of the file
      for line in content[1:]:
        movie_data = line.split(',')  # ['title', 'genre', 'watched']
        movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == 'True'))

      user = User(username)
      user.movies = movies
      return user

##Class Methods
  @classmethod
  def load_from_file(cls, filename):
    with open('{}.txt'.format(filename), 'r') as f:
      content = f.readlines()
      username = content[0]
      movies = []

      for line in content[1:]:
        movie_data = line.split(',')  # ['title', 'genre', 'watched']
        movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == 'True'))

      user = User(username)
      user.movies = movies
      return user

## Using JSON
  json.dump()
  json.load()

#argument unpacking
  ordering becomes irrelevant if you unpack the name

#in movie.py
  @classmethod
  def from_json(cls, json_data):  # {'title': '...', 'genre': '...', 'watched': True}
    return Movie(title=json_data['title'], genre=json_data['genre'], watched=json_data['watched'])

#this is the same as above
  @classmethod
  def from_json(cls, json_data):
    return Movie(**json_data) #  **json_data is a way of creating the dictionary from the json data.

# opening files in Python
  https://docs.python.org/3/library/functions.html#open


































