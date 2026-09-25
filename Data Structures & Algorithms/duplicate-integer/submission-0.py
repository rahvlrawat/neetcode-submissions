class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = dict()
        for i in nums: 
            if i in track.keys():
                track[i]+=1
                if(track[i]==2):
                    return True
            else:
                track[i]=1     
        return False        