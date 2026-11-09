from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [0]*(len(nums)+1)
        for x,y in count.items():
            if bucket[y] == 0:
                bucket[y] = [x]
            else:
                bucket[y] += [x]


            
        counter = len(bucket) - 1
        final = []
        while counter > 0:
            if bucket[counter] != 0:
                final += bucket[counter]
                if len(final) == k:
                    return final
            counter -= 1
            
        return final



