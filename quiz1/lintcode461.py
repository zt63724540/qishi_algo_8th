# Description
# Find the kth smallest numbers in an unsorted integer array.

# method 1: build max heap with size k and keep rebalance heap from k+1 to n, then the root is the kth smallest number
# and the whole heap is the k smallest numbers in an unsorted array

# method 2: quick select
def kthsmallest(arrays, l, r, k):
	if 0 < k <= r - 1 + l:
		pos = partition(arrays, l, r)

		if pos - l == k - 1:
			return arrays[pos]
		elif pos - l > k - 1:
			return kthsmallest(arrays, l, pos - 1, k)
		else:
			return kthsmallest(arrays, pos + 1, r, k - pos + l - 1)

def partition(arr, l, r):
	pivot = arr[r]
	i = l
	for j in range(l, r):
		if arr[j] <= pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[r] = arr[r], arr[i]
	return i

arrays = [5, 3, 10, 2, 8, 1]
k = 4
print(kthsmallest(arrays, 0, 5, 4))