def reihe (zahl):
	number = zahl
	a = str(number) + ' '
	for i in range(1,6):
		if number % 2 == 0:
			number = int(number / 2)
		else:
			number = int(3 * number + 1)
		a = a + str(number) + ' '	
	if number == 1:
		print(a)
		print()

print('Dieses Programm hilft 8.1 c) zu zeigen. Gibt alle Reihen mit Startwert 1 bis Maximalwert aus, bei denen a6 = 1')
print('Maximalwert eingeben:')
b = int(input())
b = b +1
for i in range (1,b):
	reihe(i)