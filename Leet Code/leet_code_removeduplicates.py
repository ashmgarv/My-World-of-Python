#Remove duplicates from sorted array
#140ms
def removeDuplicates(nums):
    index = 0
    while index < len(nums) - 1:
            if nums[index] is nums[index + 1]:
               nums.pop(index)
            else:
                index += 1
    return (len(nums))

