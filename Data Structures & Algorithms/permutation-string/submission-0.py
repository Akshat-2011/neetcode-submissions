from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1) - 1
        l = 0
        s_map = Counter(s1)
        s_set = set(s1)
        for r in range(k,len(s2)):
            substring_map = Counter(s2[l:r+1])
            if s_map == substring_map:
                return True
            l += 1
        return False

            

        