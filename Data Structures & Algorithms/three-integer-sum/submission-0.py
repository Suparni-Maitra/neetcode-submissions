class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() #sort the input array

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue 
                #check if the two elements are same and its not the first element
                #if it same then skip and continue.
            l,r= i+1, len(nums)-1
            #now do the rest of the array with twosum
            while l<r:
                threeSum=a + nums[l] + nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else: 
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res

