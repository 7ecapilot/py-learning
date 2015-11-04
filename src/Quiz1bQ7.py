import math

def polygon_area(num_sides, side_length):
	numerator = 0.25 * num_sides * side_length ** 2
	denominator = math.tan(math.pi / num_sides)
	result = numerator / denominator
	return result

number_of_sides = 7
side_length = 3
print (number_of_sides)
print (side_length)
area = polygon_area(number_of_sides, side_length)
print (area)