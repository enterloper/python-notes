class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.mark) / len(self.marks)

	def friend(self, friend_name):
		return Student(friend_name, self.school)

	@classmethod
	def working_friend(cls, origin, friend_name, *args):
		return cls(friend_name, origin.school, *args)


class WorkingStudent(Student):
	def __init__(self, name, school, salary, job_title):
		super().__init__(name, school)
		self.salary = salary
		self.job_title = job_title


anna = WorkingStudent('Anna', "Oxford", '30K', 'Software Developer')
print(anna.salary)
friend_of_anna = anna.friend('George')
working_friend_of_anna = WorkingStudent.working_friend(anna, 'Jack', 17.50, 'DevOps engineer')
print(friend_of_anna.name)
print(friend_of_anna.school)
print(working_friend_of_anna.name)
print(working_friend_of_anna.school)
print(working_friend_of_anna.salary)
