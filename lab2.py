from shapely.geometry import Polygon, Point
from itertools import product
from random import uniform
import matplotlib.pyplot as plt

def f(x, y):
	return x * x

def generate_points(polygon: Polygon, number):
	points = []
	xlo, ylo, xhi, yhi = polygon.bounds

	while len(points) < number:
		p = Point(uniform(xlo, xhi), uniform(ylo, yhi))
		if polygon.contains(p):
			points.append((p.x, p.y))

	return points

def approximate(vertices, n):
	polygon = Polygon(vertices)

	s = polygon.area

	result, avg = 0, 0
	points = generate_points(polygon, n)
	for x, y in points:
		result += f(x, y) * s / n
		avg += f(x, y) / n

	dispersion = 0
	for x, y in points:
		dispersion += (abs(f(x, y) - avg)) / (n - 1)

	error = (dispersion ** 0.5) * s / (n ** 0.5)

	return result, error

def build_error_graph(vertices):
	cur_n = 10
	n_axis = []
	error_axis = []

	while cur_n < 100000:
		n_axis.append(cur_n)
		error_axis.append(approximate(vertices, cur_n)[1])
		cur_n *= 3

	plt.xlabel("Количество случайных точек")
	plt.ylabel("Ошибка")
	plt.title("Изменение ошибки")
	plt.plot(n_axis, error_axis)
	plt.savefig("graph.png")

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
	result, error = approximate(vertices, read_int("Введите количество случайных точек внутри многоугольника: "))
	print(f"Оценка значения: {result} ± {error}")
	print("Построение графика...")
	build_error_graph(vertices)
	print("График сохранён в файл graph.png")


if __name__ == "__main__":
	main()