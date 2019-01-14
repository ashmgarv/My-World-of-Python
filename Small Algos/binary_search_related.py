import math
class SearchAlgorithms:
    def search(self,left, right, nums, target):
         if right >= left:
             mid = left + (right - 1) // 2
             if nums[mid] == target :
                 return  mid
             elif nums[mid] > target:
                return self.search(left, mid - 1,nums, target)
             return self.search(mid + 1,right,nums, target)
         return -1



    def binarySearchIterative(self, number, array):
        middle = (len(array)) // 2;
        found = False;
        while(middle != 0):
            if(number < array[middle]):
                array = array[0:middle];
                middle = (len(array) // 2);
            if(number > array[middle]):
                array = array[middle:];
                middle = (len(array) // 2);
            if(number == array[middle]):
                found = True;
                break;
            if(middle == 0 or middle == len(array)):
                found = False;
                break;
        return found;

    def newBinarySearch(self, item, myArray):
        left = 0;
        right = (len(myArray)) - 1;
        while(left <= right):
            middle = math.ceil((left + right) / 2)
            if(item == myArray[middle]):
                return True;
            elif(item < myArray[middle]):
              right = middle - 1;
            elif(item > myArray[middle]):
              left = middle + 1;
        return False;

    def srch(self,left, right, x):
        if right >= left:
            mid = (left + right) / 2
            if right * right == x:
                return int(right)
            elif mid * mid > x:
                return self.srch(left, mid / 2, x)
            d = math.floor(mid)
            ret = 1
            for i in range(d, math.floor(right)):
                if i * i is x:
                    return int(math.floor(i))
                elif i * i < x:
                    ret = i
            return int(ret)

    def sqrt(self,mid, x):
            if mid * mid == x:
                return int(mid)
            elif mid * mid > x:
                return self.sqrt(mid / 2, x)
            d = math.floor(mid)
            for i in range(d, (d * 2) +2):
                if i * i is x:
                    return int(math.floor(i))
                elif i * i > x:
                    return int(i-1)


myArr = [-1,0,5]
sAl = SearchAlgorithms();
# res = sAl.search(0,len(myArr) - 1,myArr,5)
# if(res):
# print(sAl.srch(0, 20, 40));

print(sAl.sqrt(5/2, 5))

# print (2 +3 //2)
# else:
#  print("No");

# res = sAl.binarySearchIterative(12, myArr);
# if(res):
#  print("Yes");
# else:
#  print("No");
#
# res = sAl.newBinarySearch(myArr, -34);
# if(res):
#  print("Yes");
# else:
#  print("No");
