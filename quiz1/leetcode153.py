def findMin(nums):
	if len(nums) == 1: return nums[0]
	elif nums[0] < nums[-1]: return nums[0]
	m = len(nums) // 2
	return min(self.findMin(nums[:m]), self.findMin(nums[m:]))

# Runtime: 32 ms, faster than 99.83% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.