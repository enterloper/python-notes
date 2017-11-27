students = []

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


def create_student():
	student_name = input('Enter the student\'s name: ')
	# student = {'name': student_name, 'marks': []}
	student_data = Student(student_name)

	return student_data


def add_marks_to_student(student, mark):
	student.marks.append(mark)


# def calculate_average_mark(student):
# 	number = len(student.marks)
# 	if number == 0:
# 		return 'The student {} has no marks to average!'.format(student.name)
#
# 	total = sum(student.marks)
# 	return total / number


def print_student_details(student):
	print('{}, average mark: {}'.format(student.name, student.average_mark()))


def print_student_list(student_group):
	if len(student_group) == 0:
		print('There are currently no students in the class.')
	for i, student in enumerate(student_group):
		print("ID: {}".format(i))
		print_student_details(student)


def menu(student_list):
	selection = input("Enter 'p' to print the student list, "
					"'s' to add a new student, "
					"'a' to add a mark to a student, "
					"or 'q' to quit. "
					"Enter your selection: ")
	while selection != 'q':
		if selection == 'p':
			print_student_list(student_list)
		elif selection == 's':
			student_list.append(create_student())
		elif selection == 'a':
			student_id = int(input("Enter the student ID to add a  mark to: "))
			student = student_list[student_id]
			new_mark = int(input('Add student\'s new mark to be added: '))
			add_marks_to_student(student, new_mark)

		selection = input("Enter 'p' to print the student list, "
						  "'s' to add a new student, "
						  "'a' to add a mark to a student, "
						  "or 'q' to quit. "
						  "Enter your selection: ")

menu(students)
