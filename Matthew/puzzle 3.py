import helper
import re

PATH = './Matthew/Puzzle Inputs/puzzle 3.txt'

@helper.timer
def main():
	text = None
	with open(PATH, 'r') as f:
		text = ''.join(f.readlines())
	
	pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
	test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

	matches = [x.replace('mul(', '').replace(')', '').replace('(', '').replace(')', '') for x in re.findall(pattern, text)]

	sum = 0
	action = 'do'
	for match in matches:
		if (match == 'do'):
			action = 'do'
		elif (match == "don't"):
			action = "don't"
		elif (action == 'do'):
			x, y = match.split(',')
			sum += int(x) * int(y)
	
	print(sum)

	

# This is an executable
if (__name__ == '__main__'):
	main()