from collections import deque


class Stack:

	def __init__(self):
		self.stack = deque()

	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		elif len(self.stack) > 0:
			return False

	def push(self, new_el):
		self.stack.append(new_el)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def size(self):
		return len(self.stack)
