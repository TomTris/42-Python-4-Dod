import pandas as pd

def mean(li : list):
	a = 0.0
	cnt = 0
	for nbr in li:
		a += nbr
		cnt += 1
	if cnt == 0:
		print("Error")
		return None
	return print(f"mean : {float(a / cnt)}")


def median(li : list):
	cnt = 0
	for nbr in li:
		cnt += 1
	if cnt == 0:
		print("Error")
		return None
	if cnt % 2 == 1:
		return print(f"median : {li[cnt // 2]}")
	else:
		a = li[cnt // 2] + li[cnt // 2 - 1]
		return print(f"median : {float(a / 2)}")


def quartile(li : list):
	cnt = 0
	for nbr in li:
		cnt += 1
	if cnt == 0:
		print("Error")
		return None
	cnt -= 1
	cnt1 = cnt
	ret = []

	cnt = float(cnt / 4 * 3)
	if cnt % 1 == 0:
		ret.append(float(li[int(cnt)]))
	else:
		a = int(cnt)
		b = a + 1
		cnt -= a
		c = float(a * cnt + b * (1 - cnt))
		ret.append(c)
	
	cnt = cnt1
	cnt = float(cnt / 4)
	if cnt % 1 == 0:
		ret.append(float(li[int(cnt)]))
	else:
		a = int(cnt)
		b = a + 1
		cnt -= a
		c = float(a * cnt + b * (1 - cnt))
		ret.append(c)
	print(f"quartile : {ret}")


def std(li : list):
	a = 0.0
	cnt = 0
	for nbr in li:
		a += nbr
		cnt += 1
	if cnt == 0:
		print("Error")
		return None
	mean = float(a / cnt)
	
	sum = 0
	for nbr in li:
		sum += ((nbr - mean)**2)
	sum = sum / cnt
	return print(f"std : {sum ** 0.5}")

def var(li : list):
	a = 0.0
	cnt = 0
	for nbr in li:
		a += nbr
		cnt += 1
	if cnt == 0:
		print("Error")
		return None
	mean = float(a / cnt)
	
	sum = 0
	for nbr in li:
		sum += ((nbr - mean)**2)
	sum = sum / cnt
	return print(f"var : {sum}")

def ft_statistics(*args_o, **kwargs) -> None:
	args1 = list(args_o)
	keys = list(kwargs.keys())
	
	cnt = 0
	args = []
	for nbr in args1:
		if nbr.__class__.__name__ != int and nbr.__class__ != int:
			print("ERROR")
			return
		cnt += 1
	while cnt > 0:
		to_add = args1[0]
		for nbr in args1:
			if nbr > to_add:
				to_add = nbr
		args.append(to_add)
		args1.remove(to_add)
		cnt -= 1
	
	for key in keys:
		if kwargs[key] == "mean":
			mean(args)
		elif kwargs[key] == "median":
			median(args)
		elif kwargs[key] == "quartile":
			quartile(args)
		elif kwargs[key] == "std":
			std(args)
		elif kwargs[key] == "var":
			var(args)

def main():
	ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
	print("-----")
	ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
	print("-----")
	ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
	print("-----")
	ft_statistics(toto="mean", tutu="median", tata="quartile")

if __name__ == "__main__":
	main()