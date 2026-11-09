from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_keys = heapq.nlargest(k, count, key=count.get)
        return top_keys
