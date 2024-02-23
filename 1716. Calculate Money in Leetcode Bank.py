class Solution(object):
    def totalMoney(self, n):
        ans =0
        mon_count = 0

        for i in range(1,n+1): #in the range of number of days given
            day = i%7 #1=monday, 2=tuesday and so on..
            if day%7==0: #if the day is sunday
                day += 7 #increments day by 7 to represent monday
            ans += mon_count+day #since every day the count if increementing
            if i%7==0: #if it is a sunday
                mon_count+=1
        return ans
