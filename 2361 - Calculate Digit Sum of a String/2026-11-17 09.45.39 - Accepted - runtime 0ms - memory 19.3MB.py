class Solution:
    def digitSum(self, s: str, k: int) -> str:
        slen=len(s)
        
        while slen>k:
            newString=""
            for i in range(0,slen,k):
                chunk=s[i:i+k]
                sum=0
                for c in chunk:
                    sum+=int(c)
                newString+=str(sum)
            
            s=newString
            slen=len(s)
        
        return s

