def twoSum(nums, target):
    newSorted = nums[:]
    newSorted.sort()
    indices = []
    for i in range(0, len(nums)):
        start = newSorted[i]
        l = i
        indices = []
        r = len(nums) - 1
        while (l <= r):
            m = (l + r) // 2
            if (start + newSorted[m]) == target:
                if(start == newSorted[m]):
                    indicesz = [i for i, x in enumerate(nums) if x == start]
                    i = indicesz[0]
                    m = indicesz[1]
                else:
                    i = nums.index(newSorted[i])
                    m = nums.index(newSorted[m])
                indices = [i,m]
                break
            elif start + newSorted[m] > target:
                r = m - 1
            elif start + newSorted[m] < target:
                l = m + 1
        if len(indices) is not 0:
            break;

    return indices


res = twoSum([5,7,11,15,6,78,200,79,34], 215)
print(res)