def addition(arg1, arg2, arg3, arg4):
	return arg1 + arg2 + arg3 + arg4


def addition_simplified(*args):
	return sum(args)


def what_are_kwargs(*args, **kwargs):
	print(args)
	print(kwargs)


def another_kwargs(name, location):
	print(name)
	print(location)


what_are_kwargs(12, 34, 56, name="Rich", location="Dallas, TX")
another_kwargs(location="Flagstaff, AZ")
