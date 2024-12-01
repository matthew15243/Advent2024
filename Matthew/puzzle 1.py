import Matthew.helper as helper
import numpy as np

PATH = './Puzzle Inputs/puzzle 1-1.txt'

@helper.timer
def main():
	values1 = []
	values2 = []
	with open(PATH, 'r') as f:
		while True:
			try:
				v1, v2 = f.readline().split()
			except:
				break

			values1.append(int(v1))
			values2.append(int(v2))
	
	values1 = np.array(values1)
	values2 = np.array(values2)

	values1.sort()
	values2.sort()
	values = np.abs(values2 - values1)

	print(np.sum(values))
	

# This is an executable
if (__name__ == '__main__'):
	main()