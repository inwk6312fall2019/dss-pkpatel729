num = [[1,4,5], [3], [4, 5, 6]]


def nested_sum(p):

	total = 0

	for i in p:

		for j in i:
			total += j

	print(total)

nested_sum(num)
