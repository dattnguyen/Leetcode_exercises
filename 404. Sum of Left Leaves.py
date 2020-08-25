# Find the sum of all left leaves in a given binary tree.

def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if not root:  # base case is the node is empty
        return 0
    # intuition is: we check the left node and see if its children (left and right) are both null
    # which means the left node is a leaf node
    # we can update the count with its value and recursion on the right side
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + self.sumOfLeftLeaves(root.right)

    # if the left node does have children (which means it's not a leaf node) we recursion on both sides
    else:
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)