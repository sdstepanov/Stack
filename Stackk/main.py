from Stack import Stack


def balanced(string):
	start = "([{"
	finish = ")]}"
	stack = Stack()
	balance = even_num(string)
	index = 0
	while index < len(string) and balance:
		symbol = string[index]
		if symbol in start:
			stack.push(symbol)
		elif stack.isEmpty():
			balance = False
		else:
			top = stack.pop()
			if start.index(top) != finish.index(symbol):
				balance = False
		index += 1
	if balance and stack.isEmpty():
		return "сбалансировано"
	else:
		return "несбалансировано"


def even_num(string):
	if len(string) % 2 == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	check_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
	for i in check_list:
		print(balanced(i))
