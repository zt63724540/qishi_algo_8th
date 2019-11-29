class Solution:
	"""
	@param n: An integer
	@param edges: a list of undirected edges
	@return: true if it's a valid tree, or false
	"""

	def validTree(self, n, edges):
		from collections import deque, defaultdict
		# write your code here
		if n <= 1: return True
		if len(edges) != n - 1: return False
		mapping = defaultdict(list)
		for edge in edges:
			u, v = edge
			mapping[u].append(v)
			mapping[v].append(u)

		queue = deque([0])
		history = set()

		while queue:
			node = queue.popleft()
			if node not in mapping: return False
			for v in mapping[node]:
				if v not in history:
					queue.append(v)
					history.add(v)

		if len(history) == n: return True
		return False

main = Solution()
print(main.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))