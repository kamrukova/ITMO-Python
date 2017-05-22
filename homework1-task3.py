xA = int(input('Введите кординату x, вершины треугольника A '))
yA = int(input('Введите кординату y, вершины треугольника A '))
xB = int(input('Введите кординату x, вершины треугольника B '))
yB = int(input('Введите кординату y, вершины треугольника B '))
xC = int(input('Введите кординату x, вершины треугольника C '))
yC = int(input('Введите кординату y, вершины треугольника C '))



ABsq = (xB - xA) ** 2 + (yB - yA) ** 2
BCsq = (xC - xB) ** 2 + (yC - yB) ** 2
CAsq = (xC - xA) ** 2 + (yC - yA) ** 2

if ABsq + BCsq == CAsq or ABsq + CAsq == BCsq or BCsq + CAsq == ABsq:
	print('Треугольник прямоугольный')

else:
	print('Треугольник не прямоугольный')
 



