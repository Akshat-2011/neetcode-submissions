from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_tups = sorted(count.items(), key = lambda x: x[1] , reverse = True)
        res = []
        for keys, _ in sorted_tups:
            if len(res) == k:
                break
            res.append(keys)
        return res



