my_list = [0, 1, 2, 3, 4]
a_doubled_list = [x * 2 for x in range(5)]  # range(5) creates a list: [0, 1, 2, 3, 4]
print(my_list, a_doubled_list)

# All evens approach
print([n for n in range(10) if n% 2 == 0])  # => [0, 2, 4, 6, 8]

# Normalise data!
people_you_know = ["Carl", " JOhn", "anna", "GREG"]
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)  # => ['carl', 'john', 'anna', 'greg']
