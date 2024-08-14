def square(x: int | float) -> int | float:
	if x.__class__ != int and x.__class__ != float:
		raise Exception("Invalid type of x")
	return x*x


def pow(x: int | float) -> int | float:
	if x.__class__ != int and x.__class__ != float:
		raise Exception("Invalid type of x")
	return x**x


def outer(x: int | float, function) -> object:
	if x.__class__ != int and x.__class__ != float:
		raise Exception("Invalid type of x")
	count = 0

	def inner() -> float:
		nonlocal count
		count += 1
		cnt = 0
		val = function(x)
		while cnt < count - 1:
			val = function(val)
			cnt += 1
		return val
	return inner
