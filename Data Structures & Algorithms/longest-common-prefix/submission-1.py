class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            chars = set()
            for x in strs:
                if i >= len(x):
                    return x
                chars.add(x[i])
                if len(chars) > 1:
                    if i == 0:
                        return ""
                    else:
                        return x[:i]
            else:
                i += 1

        

        