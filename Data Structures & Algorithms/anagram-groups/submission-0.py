class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            sorted_strs[sorted_x] = sorted_strs.get(sorted_x,[]) + [x]
        output = []
        for x in list(sorted_strs.values()):
            output.append(x)
        
        return output
        
        