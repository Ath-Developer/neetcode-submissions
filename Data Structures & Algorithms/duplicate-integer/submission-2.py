class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        d=dict(Counter(nums))
        for i in d.values():
            if i>=2:
                return True
            
        return False