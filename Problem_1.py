#Time Complexity:O(n)
# Space Complexity : O(n)
from collections import deque

class Solution:
    def levelOrder(self, root):
        result = []
        if root == None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            temp_list = []
            for i in range(0,len(queue)):
                node = queue.popleft()
                temp_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(temp_list)
        return result
            


        