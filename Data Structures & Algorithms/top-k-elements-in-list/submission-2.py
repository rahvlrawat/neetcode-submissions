class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track={}
        for i in nums: 
            track[i]=1 + track.get(i,0)
        sol=[]
        for key,value in track.items():
            sol.append([key,value])
        a=sorted(sol, key=lambda x: x[1])
        ret=[]
        while (len(ret))<k:
            ret.append(a.pop()[0])
        return ret
