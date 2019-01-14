
#The idea is to keep the first number fixed and check if the list contains other three numbers which
#sum up to be complement of difference between the first selected number and the target sum

def fourSum(nums,target):
    newList = nums[:]
    #Sort the list, necesssary because we will be doing a binary search to find the last three numbers
    newList.sort()
    ans = []
    i = 0
    k = 0
    tar = 0

    #Loop over the entire list
    while k < len(newList):
        first = newList[k]

        #Difference between first element and the target sum
        tar = target - first
        i = k + 1

        #Loop over the elements starting from the index succeeding index of the first selected number
        while i < len(newList):

            #Destination is what we are searching for, keeps changing according to the first and the next number selected
            destination = (tar - newList[i])
            left = i + 1
            right = len(newList) - 1

            #Search starts here
            while(left < right):

                sum = newList[left] + newList[right]

                #Keep shrinking the search space until a match is found
                if(sum < destination):
                    left += 1
                elif (sum > destination):
                    right -= 1
                else:
                    newFound = []
                    newFound = [first, newList[i], newList[left], newList[right]]
                    ans.append(newFound)

                    #Keep ignoring duplicates if any
                    while(left < right and newList[left] == newFound[2]):
                        left += 1
                    while (left < right and newList[right] == newFound[3]):
                        right -= 1
            # Keep ignoring duplicates if any for the indices as well
            while( i + 1 < len(newList) and newList[i] == newList[i+1]):
                i += 1
            i += 1
        while (k + 1 < len(newList) and newList[k] == newList[k + 1]):
            k += 1
        k += 1
    return ans


res = fourSum([1, 0, -1, 0, -2, 2],0)
print(res)