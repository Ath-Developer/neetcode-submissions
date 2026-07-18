class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=min(strs,key=len)
        res=''
    
        for i in range(0,len(l)):
            for j in strs:
                if l[i] != j[i]:
                    return res

            res+=l[i]
        return res
        