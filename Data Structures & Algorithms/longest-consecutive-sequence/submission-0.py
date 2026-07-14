class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for n in numset:
            if n-1 not in numset:
                length=1
                next=n+1
                while next in numset:
                    length+=1
                    next+=1
                longest=max(longest,length)
        return longest