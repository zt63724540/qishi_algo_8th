def calc(a, b, op):
	if op == "+":
		return a + b
	if op == "-":
		return a - b
	if op == "*":
		return a * b

def diffWaysToCompute(input):
	if input.isdigit():
		return [int(input)]
	res = []
	for i in range(len(input)):
		if input[i] in "+-*":
			res1 = diffWaysToCompute(input[:i])
			res2 = diffWaysToCompute(input[i+1:])
			for j in res1:
				for k in res2:
					res.append(calc(j, k, input[i]))
	return res

print(diffWaysToCompute("2*3-4*5"))
# Runtime: 28 ms, faster than 99.51% of Python3 online submissions for Different Ways to Add Parentheses.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Different Ways to Add Parentheses.