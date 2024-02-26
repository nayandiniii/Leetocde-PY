# Runtime: 68 ms, faster than 91.35% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
# Memory Usage: 14.1 MB, less than 57.56% of Python3 online submissions for Sort Integers by The Number of 1 Bits.
class Solution:
    def sortByBits(self, arr):
        arr = [(bin(i).count('1'), i) for i in arr]
        arr.sort()
        return [i[1] for i in arr]
