class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while i*i<=x:
            i+=1
        return i-1
#        while x>0:
#            for i in range(1,x):
#                if i*i==x:
#                    return int(i)
#                    