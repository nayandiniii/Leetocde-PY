class Solution(object):
    def majorityElement(self, nums):
        # Initialize count of candidate element occurrences
        count = 0
        # Initialize candidate element
        candidate = None

        # Iterate through each element in the array
        for num in nums:
            # If count is 0, update candidate to current element
            if count == 0:
                candidate = num
            # Increment or decrement count based on current element
            count += (1 if num == candidate else -1)

        # Return the candidate element, which is the majority element
        return candidate
