import helper
import re

PATH = './Matthew/Puzzle Inputs/puzzle 4.txt'

def checkLocation(puzzle, row, col):
	search = 'MAS'
	counter = 0

	if (row - 1 >= 0 and row + 1 < len(puzzle) and col - 1 >= 0 and col + 1< len(puzzle[row])):
		topLeftToBottomRight = (puzzle[row - 1][col - 1] + puzzle[row][col] + puzzle[row + 1][col + 1])
		bottomLeftToTopRight = (puzzle[row + 1][col - 1] + puzzle[row][col] + puzzle[row - 1][col + 1])

		counter += topLeftToBottomRight == search
		counter += topLeftToBottomRight[::-1] == search
		counter += bottomLeftToTopRight == search
		counter += bottomLeftToTopRight[::-1] == search
	
	if (counter == 2):
		return 1
	else:
		return 0

@helper.timer
def main():
	puzzle = None
	with open(PATH, 'r') as f:
		puzzle = [x.replace('\n', '') for x in f.readlines()]
	
	pattern = 'A'
	counter = 0
	for i, row in enumerate(puzzle):
		locations = [x.start() for x in re.finditer(pattern, row)]

		for location in locations:
			num = checkLocation(puzzle, i, location)
			counter += num
		
		# break

	print(counter)
	

	

# This is an executable
if (__name__ == '__main__'):
	main()