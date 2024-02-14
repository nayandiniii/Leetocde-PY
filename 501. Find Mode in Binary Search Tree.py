from collections import Counter

class Solution:
    def findMode(self, root):
        # Helper function to perform pre-order traversal
        def pre_order_traversal(node, nodes):
            if node is None:
                return
            # Append the value of the current node to the list
            nodes.append(node.val)
            # Recursively traverse the left subtree
            pre_order_traversal(node.left, nodes)
            # Recursively traverse the right subtree
            pre_order_traversal(node.right, nodes)
        
        # Initialize an empty list to store node values
        nodes = []
        # Perform pre-order traversal starting from the root
        pre_order_traversal(root, nodes)
        
        # Use Counter to count occurrences of each node value
        node_counter = Counter(nodes)
        # Find the maximum frequency of any node value
        max_frequency = max(node_counter.values())
        # Find all node values with the maximum frequency
        modes = [key for key, value in node_counter.items() if value == max_frequency]
        
        return modes
