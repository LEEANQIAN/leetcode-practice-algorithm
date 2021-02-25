# 13. Roman to Integer (EASY)
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol = {'I':1,'V':5,
                 'X':10, 'L': 50, 'C': 100,
                 'D': 500, 'M':1000}
        res = 0
        for index, char in enumerate(s):
            if (index + 1 < len(s)) and (symbol[char] < symbol[s[index+1]]):
                res -= symbol[char]
            else:
                res += symbol[char]
        return res
