# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def get_parent(node = root, parent = None):
            if not node: return
            hashmap[node] = parent
            get_parent(node.left, node), get_parent(node.right, node)
        
        def search(node = target, distance = 0):
            if not node or node.val in visited: return
            visited.add(node.val)
            if distance == k: answer.append(node.val)
            for neighbour in (hashmap[node], node.left, node.right):
                search(neighbour, distance+1)
        
        hashmap, answer, visited = {}, [], set()
        get_parent(), search()
        return answer