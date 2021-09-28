class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        b=[]
        for s in strs:
            z,o=0,0
            for ch in s:
                if ch == "0":z+=1
                else:o+=1
            b.append([z,o])
        
        @cache
        def r(i,mc,nc):
            if i==len(b) or (mc==0 and nc==0):return 0
            add=0
            if b[i][0]<=mc and b[i][1]<=nc:add=1+r(i+1,mc-b[i][0],nc-b[i][1])
            return max(add,r(i+1,mc,nc))
                
            
        return r(0,m,n)
        
        
        
        
        
        
      #  Success
#Details 
#Runtime: 2176 ms, faster than 89.14% of Python3 online submissions for Ones and Zeroes.
#Memory Usage: 194.2 MB, less than 18.33% of Python3 online submissions for Ones and Zeroes.
