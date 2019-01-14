#LeetCode Longest Common Prefix
#52ms
#Faster than 98% of Python submissions

def longestComonPrefix(strs):
        length = 0
        i = -1
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        str1 = strs[length]
        str2 = strs[length + 1]
        while (i < len(str1) - 1) and (i < len(str2) - 1):
            if str1[i + 1] == str2[i + 1]:
                i += 1
            else:
                break
        strMatch = strs[0][:i + 1]
        if i is not -1 and len(strs) > 2:
            lengthOfArray = len(strs)
            d = 2
            while d <= lengthOfArray - 1:
                if strs[d][:i + 1] is strMatch:
                    d += 1
                    continue
                else:
                    f = -1
                    while f < len(strMatch) and f < len(strs[d]):
                        if strs[d][:f + 2] == strMatch[:f + 2]:
                            f += 1
                        else:
                            break
                    if f is -1:
                        strMatch = ""
                        break
                    else:
                        strMatch = strMatch[:f + 1]
                        d += 1
            return strMatch
        elif i is not -1:
            return strMatch
        else:
            return ""


a = longestComonPrefix( ["a","a","a"])
print(a)