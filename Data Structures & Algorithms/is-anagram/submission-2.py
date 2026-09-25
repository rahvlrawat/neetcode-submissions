class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=len(s)
        if(sl!=len(t)): 
            return False
        tracks=dict()
        trackt=dict()
        for i in range(0,sl):
            if s[i] not in tracks.keys():
                tracks[s[i]]=1
            else:
                tracks[s[i]]+=1   
            if t[i] not in trackt.keys():
                trackt[t[i]]=1
            else:
                trackt[t[i]]+=1
        if(tracks==trackt):
            return True
        return False                       
            