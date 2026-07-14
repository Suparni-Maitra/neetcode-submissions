class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=[]
        res=[]
        temp=set(nums)
        for num in temp:
            l=[]
            l.append(nums.count(num))
            l.append(num)
            arr.append(l)
        arr.sort()
        for i in range (0,k):
            res.append(arr.pop()[1])
        return res

