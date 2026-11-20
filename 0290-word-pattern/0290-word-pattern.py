class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        S=s.split()
        if len(pattern) != len(s.split()):
            return False

        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != S[i]:
                    return False
            else:
                if S[i] in hashmap.values():
                    return False

                hashmap[pattern[i]] = S[i]

        return True
