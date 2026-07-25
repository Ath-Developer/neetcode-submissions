class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in t:
            if j in d:
                d[j]-=1
            elif j not in d:
                d[j]=1

        for k in d.values():
            if k>=1:
                return False
            
        return True
        