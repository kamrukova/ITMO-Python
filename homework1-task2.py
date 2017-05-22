plates = int(input('Колическтво тарелок: '))
gel = int(input('Моющее средство: '))

while plates > 0 and gel >= 0.5:
	plates -= 1
	gel -= 0.5
	
	print('У вас осталось', gel, 'геля')

if plates == 0: 
	print('У вас осталось', gel, 'геля')
elif gel == 0:
	print('У вас осталось', plates, 'тарелок')
	







