"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q = [node]
        mapping = {node: Node(node.val,[])}
        while q:
            n = q.pop(0)
            for i in n.neighbors:
                if i not in mapping:
                    mapping[i] = Node(i.val,[])
                    q.append(i)
                mapping[n].neighbors.append(mapping[i])
        return mapping[node]


# Runtime: 40 ms, faster than 82.88% of Python3 online submissions for Clone Graph.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Clone Graph.