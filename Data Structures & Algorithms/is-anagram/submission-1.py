class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)==len(t)):
            track=dict()
            for i in range(0,len(s)):
                if s[i] not in t:
                    return False
                else:
                    if s[i] in track:
                        track[s[i]]+=1
                    else: 
                        track[s[i]]=1
                    if t[i] in track:
                        track[t[i]]-=1
                    else: 
                        track[t[i]]=-1
            for i in track.values():
                if i!=0:
                    return False
            return True                            
        else:
            return False    