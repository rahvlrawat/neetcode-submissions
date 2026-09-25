class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = dict()
        for i in nums:
            if(track.get(i)):
                return True
            else:
                track[i]=1
        return False            