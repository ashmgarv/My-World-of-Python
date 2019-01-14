#LeetCode reverse integer
#28ms
#Faster than 100% of Python submissions
def revNum(n):
    def reverse(self, n):
        k = str(n)
        s = k[0]
        ans = 0
        if s is '-':
            g = k.replace('-', '', 1)[::-1]
            t = '-' + g
            ans = int(t)
        else:
            g = k[::-1]
            ans = int(g)
        if ans < -pow(2, 31) or ans > (pow(2, 31) - 1):
            return 0
        else:
            return ans
        
ans = revNum(1534236469)
print(ans)