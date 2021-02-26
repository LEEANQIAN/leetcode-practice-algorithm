# 20. Valid Parentheses (EASY)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rule = {'(':')', '[':']', '{':'}'}
        temp = []
        
        # if the length of s is not even, we get false
        if len(s) % 2 != 0:
            return False
        
        for i in s:
            if i in rule.keys():
                temp.append(i)
            # if temp is not empty and the current character match the
            # closing of the most recent opening, we find a match and
            # pop the most recent opening out
            elif temp and i == rule[temp[-1]]:
                temp.pop()
            else:
            # if the curent closing character is not the closing match with
            # the most recent opening, return false
                return False
        # if at the end we still have openings in temp, return false
        if len(temp) != 0:
            return False
        
        return True


        