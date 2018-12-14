def reihe (zahl):
	number = zahl
	a = str(number) + ' '
	for i in range(1,12):
		if number % 2 == 0:
			number = int(number / 2)
		else:
			number = int(3 * number + 1)
		a = a + str(number) + ' '	
	print(a)
	print()

print('Dieses Programm hilft 8.1 a) zu berechnen. Berechnet die ersten 12 Glieder')
print('Startwert eingeben:')
b = int(input())
reihe(b)