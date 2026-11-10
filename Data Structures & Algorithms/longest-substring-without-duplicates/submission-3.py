class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,1
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1    
        unc=set(s[l])
        maxP=0
        while r<len(s):
            if s[r] not in unc:
            
                maxP=max(maxP,r-l+1)
                unc.add(s[r])
                r+=1
            else:
                unc.remove(s[l])
                l+=1
                
        return maxP    
                