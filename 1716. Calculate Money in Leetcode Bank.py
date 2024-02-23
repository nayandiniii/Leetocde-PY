class Solution(object):
    def totalMoney(self, n):
        ans =0
        mon_count = 0

        for i in range(1,n+1):
            day = i%7
            if day%7==0:
                day += 7 #increments day by 7 to represent monday
            ans += mon_count+day
            if i%7==0:
                mon_count+=1
        return ans
