import helper

PATH = './Matthew/Puzzle Inputs/puzzle 5.txt'

@helper.timer
def main():
	pageOrders = {}
	# Process the page orders
	with open(PATH, 'r') as f:
		while True:
			order = f.readline()
			if (order != '' and order != '\n'):
				first, last = order.replace('\n', '').split('|')
				if (first not in pageOrders):
					pageOrders[first] = {'comesBefore' : [], 'comesAfter' : [last]}
				else:
					pageOrders[first]['comesAfter'].append(last)
				
				if (last not in pageOrders):
					pageOrders[last]  = {'comesBefore' : [first], 'comesAfter' : []}
				else:
					pageOrders[last]['comesBefore'].append(first)
			else:
				break
		
		sum = 0
		while True:
			pages = f.readline()
			if (pages != ''):
				pages = pages.replace('\n', '').split(',')
				success = True
				for i, page in enumerate(pages):
					if (page in pageOrders):
						overlap = [x for x in pageOrders[page]['comesAfter'] if x in pages[:i]]
						if (len(overlap) > 0):
							success = False
							break
				
				sum += int(pages[(len(pages) // 2)]) if success else 0
			else:
				break
		
		print(sum)
	

# This is an executable
if (__name__ == '__main__'):
	main()