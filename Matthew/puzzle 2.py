import helper

PATH = './Matthew/Puzzle Inputs/puzzle 2.txt'

def processExperiment(levels, retryCount = 0):
	# Convert values to integers
	values = [int(x) for x in levels]

	# Check for increasing
	if (values[1] > values[0]):
		for i in range(len(values) - 1):
			if (values[i + 1] > values[i] + 3 or values[i + 1] < values[i] + 1):
				if (retryCount == 0):
					tmp = values[:]
					del tmp[i]
					result = processExperiment(tmp, 1)
					if (not result):
						tmp = values[:]
						del tmp[i + 1]
						result = processExperiment(tmp, 1)
						return result if result else processExperiment(values[1:], 1)
					else:
						return True
				else:
					return False
		return True

	# Check for decreasing
	elif (values[1] < values[0]):
		for i in range(len(values) - 1):
			if (values[i + 1] > values[i] - 1 or values[i + 1] < values[i] - 3):
				if (retryCount == 0):
					tmp = values[:]
					del tmp[i]
					decreasing = processExperiment(tmp, 1)
					if (not decreasing):
						tmp = values[:]
						del tmp[i + 1]
						result = processExperiment(tmp, 1)
						return result if result else processExperiment(values[1:], 1)
					else:
						return True
				else:
					return False
		return True
	
	# Same
	elif (retryCount == 0):
		tmp = values[1:]
		equal = processExperiment(tmp, 1)
		if (equal):
			return True
		else:
			tmp = values[:]
			del tmp[1]
			return processExperiment(tmp, 1)
	else:
		return False
	

@helper.timer
def main():
	numValid = 0
	with open(PATH, 'r') as f:
		while True:
			values = f.readline().split()

			if (len(values) != 0):
				result = processExperiment(values)
				# print(f"{values} : {result}")
				numValid += result
			else:
				break;


	print(numValid)

# This is an executable
if (__name__ == '__main__'):
	main()