
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        d={}

        def clone(node):
            if node in d:
                return d[node]
            
            copy=Node(node.val)
            d[node]=copy

            for ne in node.neighbors:
                copy.neighbors.append(clone(ne))
                return copy
            
            return clone(node) if node else None


 