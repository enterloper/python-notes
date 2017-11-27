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