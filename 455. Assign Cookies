class Solution(object):
    def findContentChildren(self, g, s):
        # Sort the arrays in ascending order
        g.sort()
        s.sort()
        
        # Initialize pointers and count
        i = 0  # Pointer for greed factor array
        j = 0  # Pointer for cookie sizes array
        count = 0  # Count of content children
        
        # Iterate through the arrays
        while (i < len(g)) and (j < len(s)):
            # If the current cookie size is sufficient for the current child's greed factor
            if g[i] <= s[j]:
                # Assign the cookie to the child
                count += 1
                # Move to the next child and cookie
                i += 1
                j += 1
            else:
                # If the current cookie size is not sufficient, try the next cookie
                j += 1
        
        # Return the count of content children
        return count
