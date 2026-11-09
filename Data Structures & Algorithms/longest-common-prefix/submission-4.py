class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long = max(strs)
        short = min(strs)
        for i in range(len(short)):
            if short[i] != long[i]:
                return short[:i]
        return short


        

        