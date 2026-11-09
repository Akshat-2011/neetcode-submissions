class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_tup = set(nums)
        if len(new_tup) == len(nums):
            return False
        else:
            return True
        
        