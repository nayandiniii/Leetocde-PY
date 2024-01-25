class Solution(object):
    def uniqueOccurrences(self, arr):
#sort the array to find unique values in optimized way
        arr.sort()
        i = 0
        store = [] #to store the count of values

        while i < len(arr):
            count = 1  # initializing count as 1 for every unique element
            while i + 1 < len(arr) and arr[i] == arr[i + 1]:
                count += 1
                i += 1 #increemented to move to next element
            store.append(count)
            i += 1 #increemented to move to next element
        store.sort()
        #iterate through the count list to check for uniqueness
        for i in range(1, len(store)):
            if store[i] == store[i - 1]:
                return False  # If any two counts are equal, return False
#we write false out because if we don't then the loop will end and it will not check all the elements but first two only
        return True  # If all counts are unique, return True

```
