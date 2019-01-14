#LeetCode:Remove Element
#60ms
#Faster than 74%
class Solution:
    def removeElement(self, nums, val):

        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return len(nums)