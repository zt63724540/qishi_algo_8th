class Solution:
	def shortestPathAllKeys(self, grid: List[str]) -> int:
		m = len(grid)
		n = len(grid[0])
		numOfKeys = 0
		visited = set()
		dic = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		# find the starting point and number of keys for the initial state
		for i in range(m):
			for j in range(n):
				if grid[i][j] == '@':
					start_i = i
					start_j = j
				elif grid[i][j] in "abcdef":
					numOfKeys += 1

		# queue is used to record the possible path and corresponding status
		queue = collections.deque()
		queue.append([start_i, start_j, 0, ".@abcdef", 0])

		while queue:
			# i,j is the current location, step is the current number of moves,
			# locks contain the locks that can be opened, num is the number of collected keys
			i, j, step, locks, num = queue.popleft()

			if grid[i][j] in "abcdef" and grid[i][j].upper() not in locks:
				locks += grid[i][j].upper()
				num += 1

			if num == numOfKeys:
				return step

			# search the possible path within 4 directions and update the queue
			for x, y in dic:
				n_i = i + x
				n_j = j + y
				if 0 <= n_i < m and 0 <= n_j < n and grid[n_i][n_j] in locks:
					if (n_i, n_j, locks) not in visited:
						visited.add((n_i, n_j, locks))
						queue.append([n_i, n_j, step + 1, locks, num])
		return -1


# Runtime: 528 ms, faster than 30.49% of Python3 online submissions for Shortest Path to Get All Keys.
# Memory Usage: 20.1 MB, less than 50.00% of Python3 online submissions for Shortest Path to Get All Keys.