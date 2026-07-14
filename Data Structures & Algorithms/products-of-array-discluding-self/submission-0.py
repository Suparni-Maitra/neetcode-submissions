class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        res=[]
        #getting the product of nonzero numbers
        for i in nums:
            if i!=0:
                prod=prod*i
        if nums.count(0)==0:
            for i in nums:
                res.append(prod//i)
            return res
        elif nums.count(0)==1:
            for i in nums:
                if i!=0:
                    res.append(0)
                else:
                    res.append(prod)
            return res
        else:
            for i in nums:
                res.append(0)
            return res
