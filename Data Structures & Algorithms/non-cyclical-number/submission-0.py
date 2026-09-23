class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumofsquares(n)
            if n==1:
                return True
        return False 
        
    def sumofsquares(self,n:int)->int:
            res=0
            while n:
                ones=n%10
                res+=ones**2
                n=n//10
            return res

