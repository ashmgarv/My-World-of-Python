def threeSumZero(nums):
    newList1 = nums[:]
    left = 0;
    newList1.sort()
    ansList = []
    there = False
    indexe = 0
    firstTwoElements = []
    for i,k in enumerate(newList1):
                if curft not in firstTwoElements:
                    g = k + newList1[l]
                    nl = newList1[l + 1:len(newList1)]
                    if (-g) in nl:
                        firstTwoElements.append(curft)
                        there = False
                        from itertools import permutations
                        perm = permutations([k, newList1[l], -g])
                        for p in perm:
                            p = list(p)
                            if p in ansList:
                                there = True
                                break
                        if not there:
                            sorted = [k, newList1[l], -g]
                            sorted.sort()
                            ansList.insert(indexe, sorted)
                            indexe += 1
    return ansList


ans = threeSumZero([-1,0,1,2,-1,-4])
print(ans)