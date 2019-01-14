#LeetCode SearchInsert
#Timing: 56ms
#Faster than 88.42% of Python3 submissions
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
             ind =  [index for index, number in enumerate(nums) if number > target]
             if len(ind) > 0:
                return ind[0]
             else:
                return len(nums)


