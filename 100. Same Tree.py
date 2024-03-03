class Solution(object):
    def isSameTree(self, p, q):
        # If both trees are None, they are the same
        if not p and not q:
            return True
        # If one of the trees is None while the other isn't, they are different
        if not p or not q:
            return False
        # If the values of the current nodes are different, they are different trees
        if p.val != q.val:
            return False
        
        # Recursively check the left subtree and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
