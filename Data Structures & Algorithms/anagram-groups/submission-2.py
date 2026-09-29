class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track={}
        sol=[]
        for word in strs:
            wsort = "".join(sorted(word))
            #print(f"Actual word is '{word}' and then sort is {wsort}")
            if wsort in track:
                track[wsort].append(word)
            else:
                #print(f"hello {wsort}")
                track[wsort]=[word]
        for trackv in track.values():
            sol.append(trackv)
        return sol     

            