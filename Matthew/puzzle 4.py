import helper
import re

PATH = './Matthew/Puzzle Inputs/puzzle 4.txt'

def checkLocation(puzzle, row, col):
	search = 'XMAS'
	counter = 0

	# Search horizontally after
	if (col + 3 < len(puzzle[row])):
		counter += puzzle[row][col:col + 4] == search

	# Search horizontally before
	if (col - 3 >= 0):
		counter += puzzle[row][col - 3:col + 1][::-1] == search

	# Search Vertically above
	if (row - 3 >= 0):
		counter += (puzzle[row - 3][col] + puzzle[row - 2][col] + puzzle[row - 1][col] + puzzle[row][col])[::-1] == search

	# Search Vertically below
	if (row + 3 < len(puzzle)):
		counter += (puzzle[row][col] + puzzle[row + 1][col] + puzzle[row + 2][col] + puzzle[row + 3][col]) == search

	# Search diagonally NW (need to check)
	if (row - 3 >= 0 and col - 3 >= 0):
		counter += (puzzle[row][col] + puzzle[row - 1][col - 1] + puzzle[row - 2][col - 2] + puzzle[row - 3][col - 3]) == search

	# Search diagonally SE (need to check)
	if (row + 3 < len(puzzle) and col + 3 < len(puzzle[row])):
		counter += (puzzle[row][col] + puzzle[row + 1][col + 1] + puzzle[row + 2][col + 2] + puzzle[row + 3][col + 3]) == search

	# Search diagonally NE (need to check)
	if (row - 3 >= 0 and col + 3 < len(puzzle[row])):
		counter += (puzzle[row][col] + puzzle[row - 1][col + 1] + puzzle[row - 2][col + 2] + puzzle[row - 3][col + 3]) == search

	# Search diagonally SW (need to check)
	if (row + 3 < len(puzzle) and col - 3 >= 0):
		counter += (puzzle[row][col] + puzzle[row + 1][col - 1] + puzzle[row + 2][col - 2] + puzzle[row + 3][col - 3]) == search

	return counter

@helper.timer
def main():
	puzzle = None
	with open(PATH, 'r') as f:
		puzzle = [x.replace('\n', '') for x in f.readlines()]
	
	pattern = 'X'
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