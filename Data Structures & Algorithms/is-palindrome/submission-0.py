class Solution:
    def isPalindrome(self, s: str) -> bool:
        original=s.lower()
        i,j=0,len(original)-1
        while i<j:
            if(not original[i].isalnum()):
                i+=1
            elif not original[j].isalnum():
                j-=1
            else:
                if(original[i]!=original[j]):
                    return False
                else:
                    i+=1
                    j-=1
        return True                
