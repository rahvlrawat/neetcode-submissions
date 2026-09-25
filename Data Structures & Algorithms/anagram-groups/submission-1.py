class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track={}
        for s in strs:
            key=''.join(sorted(s))
            if key not in track:
                track[key]=[]
            track[key].append(s)
        return list(track.values())    
