class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        premult=1
        suffmult=1
        for i in range(1,len(nums)):
            premult*=nums[i-1]
            prefix.append(premult)

        for i in range(1,len(nums)):
            suffmult*=nums[len(nums)-i]
            suffix.append(suffmult)
        suffix.reverse()
        sol=[]
        for i in range(0,len(suffix)):
            sol.append(suffix[i]*prefix[i])
        return sol        
              


