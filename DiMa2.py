def reihe (zahl):
	number = zahl
	a = str(number) + ' '
	while not number == 1:
		if number % 2 == 0:
			number = int(number / 2)
		else:
			number = int(3 * number + 1)
		a = a + str(number) + ' '	
	print(a)
	print()

print('Dieses Programm hilft 8.1 b) zu zeigen. Berechnet alle Ketten mit Startwert von 1 bis Maximalwert, bis diese 1 erreichen')
print('Maximalwert eingeben:')
b = int(input())
b = b +1
for i in range (1,b):
	reihe(i)