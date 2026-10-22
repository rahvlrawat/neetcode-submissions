class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,num  in enumerate(numbers):
            rem=target-num
            if rem in seen:
                return [seen[rem],i+1]
            seen[num]=i+1    