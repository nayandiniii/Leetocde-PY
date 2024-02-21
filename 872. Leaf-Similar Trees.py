class Solution:
    def leafSimilar(self, root1, root2):
        nodeList1 = []
        nodeList2 = []
        self.findLeafDfs(root1, nodeList1)
        self.findLeafDfs(root2, nodeList2)
        return nodeList1 == nodeList2

    def findLeafDfs(self, node, nodeList):
        if not node:
            return
        if not node.left and not node.right:
            nodeList.append(node.val)
        else:
            self.findLeafDfs(node.left, nodeList)
            self.findLeafDfs(node.right, nodeList)
