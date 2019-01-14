def threeSumZero(nums,target):
    newList1 = nums[:]
    newList1.sort()
    ans = []
    i = 0
    while i < len(newList1):
        destination = (target - newList1[i])
        left = i + 1
        right = len(newList1) - 1

        while(left < right):
            sum = newList1[left] + newList1[right]

            if(sum < destination):
                left += 1
            elif (sum > destination):
                right -= 1
            else:
                newFound = []
                newFound = [newList1[i], newList1[left], newList1[right]]
                ans.append(newFound)
                while(left < right and newList1[left] == newFound[1]):
                    left += 1
                while (left < right and newList1[right] == newFound[2]):
                    right -= 1
        while( i + 1 < len(newList1) and newList1[i] == newList1[i+1]):
            i += 1
        i += 1
    return ans


res = threeSumZero([-1,0,1,2,-1,-4],2)
print(res)