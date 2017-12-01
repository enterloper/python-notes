def methodception(another):
	return another()


def add_two_numbers():
	return 44 + 56


print(methodception(add_two_numbers))
# print(methodception(lambda: 34 + 56))

# IIFE
(lambda x: x * 3)(5)

my_list = [13, 56, 77, 484]
# my_list.remove(13)
print('using lambda:', list(filter(lambda x: x != 13, my_list)))


# Above is same as :
def not_thirteen(x):
	return x != 13


# Above also is same as :
print('using for loop style, List Comprehension:', [x for x in my_list if x != 13])
print('using regular function:', list(filter(not_thirteen, my_list)))
