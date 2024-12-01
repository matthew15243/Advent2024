import time
from functools import wraps

def timer(func):

	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = func(*args, **kwargs)
		end = time.perf_counter()

		print(f"{__name__} took {end - start} seconds")

		return result

	return wrapper