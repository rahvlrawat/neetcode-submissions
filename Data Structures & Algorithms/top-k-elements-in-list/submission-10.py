class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=dict()
        for i in nums:
            a[i]=a.get(i,0)+1
        so= sorted(a.keys(),key=lambda x:a[x],reverse=True)
        return so[:k]
