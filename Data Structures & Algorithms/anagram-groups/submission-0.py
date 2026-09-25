class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track=defaultdict(list)
        for s in strs:
            key=''.join(sorted(s))
            track[key].append(s)
        return list(track.values())    
