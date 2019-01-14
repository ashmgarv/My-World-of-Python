#LeetCode Roman to Integer
#200ms
#Faster than 98% of Python Sybmissions
def romanToInt(s):
    ans = 0
    k = 0
    while k <= len(s) - 1:
        d = 0
        g = k
        if s[g] is 'I':
            if((g + 1) < len(s)):
                if (s[g + 1] is 'V'):
                    g = g + 2
                    d = 4
                elif (s[g + 1] is 'X'):
                    g = g + 2
                    d = 9
                else:
                    d = 1
            else:
                d = 1
        elif s[g] is 'V':
            ret = 5
            if ((g + 1) < len(s)):
                while (g + 1) < len(s) and s[g + 1] is 'I':
                    ret = ret + 1
                    g = g + 1
                g = g + 1
                d = ret
            else:
                d = ret
        elif s[g] is 'X':
            if ((g + 1) < len(s)):
                if (s[g + 1] is 'L'):
                    g = g + 2
                    d = 40
                elif (s[g + 1] is 'C'):
                    g = g + 2
                    d = 90
                else:
                    d = 10
            else:
                d = 10
        elif s[g] is 'L':
            d = 50
        elif s[g] is 'C':
            if ((g + 1) < len(s)):
                if (s[g + 1] is 'D'):
                    g = g + 2
                    d = 400
                elif (s[g + 1] is 'M'):
                    g = g + 2
                    d = 900
                else:
                    d = 100
            else:
                d = 100
        elif s[g] is 'D':
            d = 500
        elif s[g] is 'M':
            d = 1000

        ans = ans + d

        if g > k:
            k = g
        else:
          k = k + 1
    return ans

ans = romanToInt("C")
print(ans)