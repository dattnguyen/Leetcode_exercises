def minDepth_bfs(self, root: TreeNode) -> int:
    # BFS
    # intuition: we go level by level. If the node doesn't have both left and right child, we know we reach the min depth
    if not root:  # corner case, root is empty
        return 0
    queue = collections.deque(
        [(root, 1)])  # add in the root and level 1. We need [] since we put in a tuple (node and level),
    # otherwise we can't unpack
    while queue:  # while queue is not empty, keep going
        node, level = queue.popleft()  # pop the node and the level to process
        if node:  # we need this to make sure the node is not null. For example
            # [1,null,2]. After popping the root, we add a null and a '2' node to the queue. Without 'if node' there won't be left and right
            if not node.left and not node.right:  # if both left and right nodes are null, we reach the minimum depth and return level

                return level

            else:  # if not, add the left and right node to queue and keep processing
                queue.append((node.left, level + 1))  # this is tuple with the node and the level
                queue.append((node.right, level + 1))
#%%
def minDepth_dfs(self, root: TreeNode) -> int:
    # DFS
    # intuition: if we see a node that has both left and right child, we call the minDepth function on both and add 1
    # (since we're going down) 1 level. We then get the min of the two functions.
    # If we see a node with left child, we call the minDepth function on that left child + 1 and vice versa

    if not root:
        return 0
    else:
        if root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)