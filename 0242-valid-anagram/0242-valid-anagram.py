class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a = sorted(s)
        # b = sorted(t)
        # if a==b:
        #     return True
        # return False

        if len(s) != len(t):
            return False
        
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True
    
        