class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            target_num = target-nums[i]
            if target_num in num_dict.keys():
                return [num_dict.get(target_num),i]
            else:
                num_dict[nums[i]] = i