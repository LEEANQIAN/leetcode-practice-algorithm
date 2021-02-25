# 7. Reverse Integer (EASY)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = str(x)
        if res[0] == '-':
            num = res[1:]
            num = num[::-1]
            res = '-' + num
        else:
            res = res[::-1]
        res = int(res)
        if ((res < -(2**31)) | (res > (2**31 - 1))):
            return 0
        return res