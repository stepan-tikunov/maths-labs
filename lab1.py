from shapely.geometry import Polygon, Point
from itertools import product

def f(x, y):
	return x * x

def approximate(vertices, interval_count):
	polygon = Polygon(vertices)

	xlo, ylo, xhi, yhi = polygon.bounds
	xst, yst = (xhi - xlo) / interval_count, (yhi - ylo) / interval_count

	result = 0
	for i, j in product(range(interval_count), range(interval_count)):
		x, y = xlo + xst * (i + .5), ylo + yst * (j + .5)
		if polygon.contains(Point(x, y)):
			result += f(x, y) * xst * yst

	return result, xst * yst

def read_int(message):
	try:
		return int(input(message))
	except:
		print("Некорректное значение")
		return read_int()

def read_vertex():
	try:
		new_vertex = list(map(float, input("Координаты вершины в формате \"<x> <y>\": ").split()))
		if len(new_vertex) != 2:
			raise ValueError()
		return new_vertex
	except:
		print("Некорректное значение, повторите ввод")
		return read_vertex()

def main():
	vertices = [read_vertex() for _ in range(read_int("Введите количество вершин многоугольника: "))]
	result, error = approximate(vertices, read_int("Введите количество интервалов разбиения: "))
	print(f"Оценка значения: {result} ± {error}")


if __name__ == "__main__":
	main()