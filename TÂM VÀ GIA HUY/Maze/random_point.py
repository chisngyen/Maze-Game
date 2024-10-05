import random
def rand(size):
	x = random.randint(0, size - 1)
	y = random.randint(0, size - 1)
	return x, y
def random_spawn(size):
	house_and_tom_x, house_and_tom_y = rand(size)
	jerry_x, jerry_y = rand(size)
	while (jerry_x, jerry_y) == (house_and_tom_x, house_and_tom_y):
		jerry_x, jerry_y = rand(size)
	return (house_and_tom_x, house_and_tom_y), (house_and_tom_x, house_and_tom_y), (jerry_x, jerry_y)