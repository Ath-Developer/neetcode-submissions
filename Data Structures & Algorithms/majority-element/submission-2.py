class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=(len(nums)//2)
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,value in d.items():
            if value>m:
                return i
