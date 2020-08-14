def maxDepth_dfs(self, root: TreeNode) -> int:
    # DFS
    # intuition: if node has both left and right child, call maxDepth function on both and get the max of the two
    # if left child is none, call the maxDepth function on the right

    if not root:  # base case/corner case
        return 0
    # else: #don't really need this part.
    #     if not root.left:
    #         return self.maxDepth(root.right) + 1
    #     elif not root.right:
    #         return self.maxDepth(root.left) + 1
    #     else:
    return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
#%%
def maxDepth_bfs(self, root: TreeNode) -> int:
    # BFS
    # intuition: if we see both nodes are null, continue check the other subtree.
    # Use queue to check level by level
    if not root:
        return 0
    queue = collections.deque([(root, 1)])

    while queue:
        node, level = queue.popleft()
        if node:
            if not node.left and not node.right:
                continue
            else:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
    return level