class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tab = {}
        threshold = len(nums) // 2
        for x in range(len(nums)):
            tab[nums[x]] = tab.get(nums[x],0) + 1
            if tab[nums[x]] > threshold:
                return nums[x]
        
        