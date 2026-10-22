class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        reduced=sorted(list(set(nums)), key=int)
        lo=len(reduced)
        res=1
        final=0
        if(lo==0):
            return 0
        for i in range(1,lo):
            if(reduced[i]==reduced[i-1]+1):
                res+=1
            else:
                final=max(res,final)
                res=1
        return max(res,final)

        
        
