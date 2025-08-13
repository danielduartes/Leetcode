class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = nums.count(0)
        for j in range(i):
            nums.append(0)
        while nums.count(0) > i:
            nums.remove(0)
            
        return nums
        