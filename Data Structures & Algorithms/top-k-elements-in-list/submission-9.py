class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track={}
        for i in nums:
            if i in track:
                track[i]+=1
            else:
                track[i]=1
        sol=sorted(track.keys(), key=lambda x: track[x], reverse=True)
        ans=[]
        for i in range(0,k):
            ans.append(sol[i])
        return ans     