import helper

PATH = './Puzzle Inputs/puzzle 1.txt'

@helper.timer
def main():
	values1 = {}
	values2 = {}
	with open(PATH, 'r') as f:
		while True:
			try:
				v1, v2 = f.readline().split()
			except:
				break

			values1[v1] = values1.get(v1, 0) + 1
			values2[v2] = values2.get(v2, 0) + 1
	
	sum = 0
	for key in values1:
		sum += int(key) * values1[key] * values2.get(key, 0)
	
	print(sum)


# This is an executable
if (__name__ == '__main__'):
	main()