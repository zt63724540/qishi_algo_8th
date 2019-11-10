# Beautiful Array

# For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
# Given N, return any beautiful array A.  (It is guaranteed that one exists.)

# Idea is from https://leetcode.com/problems/beautiful-array/discuss/186679/Odd-%2B-Even-Pattern-O(N)
# new beautiful array can be constructed by three methods: deletion, addition and multiplication
# if we have a beautiful array A, then A1 = A*2 and A2 = A*2-1 as well as B = A1+A2 are beautiful arrays
# hence once we have size n beautiful array, we can get size 2n, size 4n, size 8n until size N beautiful array

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        arr = [1]
        while len(arr) < N:
            arr = [2*e-1 for e in arr] + [2*e for e in arr]
        return [e for e in arr if e <= N]

# Runtime: 28 ms, faster than 99.58% of Python3 online submissions for Beautiful Array.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Beautiful Array.