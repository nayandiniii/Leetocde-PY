# Code
```
class Solution(object):
    def rangeSumBST(self, root, low, high):
        
        if not root:
            return 0 #if there is no root value the sum is zero

        if root.val<low:
                #that means we return the elements from right and low and high
            return self.rangeSumBST(root.right,low,high)
            
        elif root.val>high:
                #if root is greater than high then we add all small elements from left
            return self.rangeSumBST(root.left,low,high)
        else:
                #once the current value is in range we return the sum
            answer =root.val + self.rangeSumBST(root.right,low,high) +self.rangeSumBST(root.left,low,high)
            return answer
        
```
