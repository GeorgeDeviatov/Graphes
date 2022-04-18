from heapq import heappush, heappop
import random

class PriorityQueue:
	def __init__(self):
		self._container = []
	
	@property
	def empty(self):
		return not self._container
	
	def push(self,item):
		heappush(self._container,item)
	
	def pop(self):
		return heappop(self._container)
	
	def __repr__(self):
		return repr(self._container)


if __name__ == '__main__':
	queue = PriorityQueue()
	print(queue)
	for i in range(10):
		n = random.randint(0,10)
		queue.push(n)
		print(queue,n)
	print(queue)
	for j in range(3):
		print()
	while not(queue.empty):
		queue.pop()
		print(queue)
