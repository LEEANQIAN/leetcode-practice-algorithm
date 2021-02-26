# 14. Longest Common Prefix (EASY)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lengths = []
        res = ''
        if len(strs) == 0:
            return res
        for string in strs:
            lengths.append(len(string))
        for i in range(min(lengths)):
            letter = strs[0][i]
            if all(str[i] == letter for str in strs):
                res += letter
            else:
                # if there is one consecutive letter not the same, 
                # then break for all
                break
        return res