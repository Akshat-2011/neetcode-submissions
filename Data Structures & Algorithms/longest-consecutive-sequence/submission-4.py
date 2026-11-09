class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for x in numSet:
            if x-1 not in numSet:
                counter = 1
                while x+counter in numSet:
                    counter+=1
                length = max(counter,length)
        return length

        