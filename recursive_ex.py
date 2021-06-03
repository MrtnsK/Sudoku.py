a = 1
b = 0

def add(a,b):
	if a != 10:
		res = a + b
		add(res, 1)
		print(res)
	return

add(a,b)
