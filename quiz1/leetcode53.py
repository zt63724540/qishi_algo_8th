# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.

# method 1
def maxSubArray(nums):
	import math
	maxSum = -math.inf
	currSum = -math.inf
	for num in nums:
		if num > currSum and currSum < 0:
			currSum = num
		else:
			currSum += num
		if currSum > maxSum:
			maxSum = currSum
	return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Runtime: 60 ms, faster than 99.85% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.5 MB, less than 78.86% of Python3 online submissions for Maximum Subarray.

# method 2: divide and conquer
import math
def crossSum(nums,m):
	tempSum = 0; leftSum = -math.inf
	for i in range(m-1, -1, -1):
		tempSum += nums[i]
		if leftSum < tempSum:
			leftSum = tempSum
	tempSum = 0; rightSum = -math.inf
	for i in range(m, len(nums)):
		tempSum += nums[i]
		if rightSum < tempSum:
			rightSum = tempSum

	return leftSum + rightSum

def maxSubArray2(nums):
	if len(nums) <= 1:
		return nums[0]
	m = len(nums)//2
	return max(maxSubArray2(nums[:m]), maxSubArray2(nums[m:]), crossSum(nums,m))

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray2(nums))

# Runtime: 124 ms, faster than 5.02% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.6 MB, less than 71.54% of Python3 online submissions for Maximum Subarray.