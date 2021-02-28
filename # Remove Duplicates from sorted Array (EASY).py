# Remove Duplicates from sorted Array (EASY)

# Method 1: del

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        if len(nums) == 0:
            return length
        
        i = 0
        j = 1
        length += 1
        while(j < len(nums)):
            if nums[j] == nums[i]:
                del nums[j]
            else:
                length += 1
                i += 1
                j += 1
        return length

# Method 2: pop

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        i = 0
        while i < len(nums)-1:
            if nums[i+1] == nums[i]:
                nums.pop(i+1)
            else:
                i += 1
        
        return len(nums)