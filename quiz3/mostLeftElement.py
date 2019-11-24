def mostLeftElement(arr, l, r, target, x):
	if r >= l:
		m = l + (r - l) // 2
		if arr[m] == x:
			target = m
			return mostLeftElement(arr, l, m-1, target, x)
		elif arr[m] > x:
			return mostLeftElement(arr, l, m-1, target, x)
		else:
			return mostLeftElement(arr, m+1, r, target, x)
	elif target == -1:
		return -1
	else:
		return target

def mostRightElement(arr, l, r, target, x):
	if r >= l:
		m = l + (r - l) // 2
		if arr[m] == x:
			target = m
			return mostRightElement(arr, m+1, r, target, x)
		elif arr[m] > x:
			return mostRightElement(arr, l, m-1, target, x)
		else:
			return mostRightElement(arr, m+1, r, target, x)
	elif target == -1:
		return -1
	else:
		return target


# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

array = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6]
x = 5
print(mostLeftElement(array, 0, len(array)-1, -1, x))
print(mostRightElement(array, 0, len(array)-1, -1, x))
