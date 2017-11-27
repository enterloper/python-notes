lottery_player = {
	'name': 'Rich',
	'numbers': (1, 76, 32, 4, 22, 16)
}


class LotteryPlayer:
	def __init__(self, name):
		self.name = name,
		self.numbers = (1, 76, 32, 4, 22, 16)

	def total(self):
		return sum(self.numbers)


player_one = LotteryPlayer('Rich')
player_two = LotteryPlayer('Hans')
print('p1-name:', player_one.name)
print('p1-total:', player_one.total())
print('p2-name:', player_one.name)
print('p2-total:', player_one.total())


# ANOTHER EXAMPLE!

class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average_from_marks(self):
		return sum(self.marks) / len(self.marks)

	@staticmethod
	def go_to_school():
		print("I'm going to school!")


anna = Student("Anna", "MIT")
anna.marks.append(56)
print(anna.marks)  # => [56]
anna.marks.append(44)  # => 50.0
print(anna.average_from_marks())
anna.go_to_school()
Student.go_to_school()