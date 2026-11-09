class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            curr_target = -nums[i]
            if curr_target < 0:
                break
            x = i + 1
            y = len(nums)-1
            while y>x:
                curr_sum = nums[x] + nums[y]
                if curr_sum > curr_target:
                    y -=1
                elif curr_sum < curr_target:
                    x +=1
                else:
                    if [nums[i],nums[x],nums[y]] not in res:
                        res.append([nums[i],nums[x],nums[y]])
                    x +=1
                    y-=1
        return res
                