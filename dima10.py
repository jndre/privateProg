for a in range (-100, 100):
	print()
	print(str(a) + ': ')
	for x in range (0, 12):
		if (a*x) % 12 == 8:
			print(str(x) + ' ')