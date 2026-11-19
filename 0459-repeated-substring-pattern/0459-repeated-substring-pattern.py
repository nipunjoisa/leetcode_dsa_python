class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        def checksubstring(substring:str) -> bool:
            m = len(substring)
            for i in range(0,n,m):
                for j in range(m):
                    if s[i+j] != substring[j] :
                        return False
            return True

                
        #To extract substring. 

        for i in range(1,(n//2)+1):
            if n%i == 0:
                substring = s[:i]
                print(substring)
                if checksubstring(substring):
                    return True 

        return False
