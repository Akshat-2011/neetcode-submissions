class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for x in s:
            s_dict[x] = s_dict.get(x,0) + 1
        t_dict = {}
        for x in t:
            t_dict[x] = t_dict.get(x,0) + 1
        if s_dict == t_dict:
            return True
        else:
            return False
        
        