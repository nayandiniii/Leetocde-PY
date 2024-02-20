#use the basic Fibonacci series rule since the number of steps for 1 stair is 1 and for 2 stairs is 2 , we follow up by using fibonacci rule

# if a,b=0 : c=a+b ; a=b ; b-c ;

class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        
        pre =1
        pro =2

        steps=0
        for i in range(2,n):
            steps=pre+pro
            pre=pro
            pro=steps

        return steps
        
