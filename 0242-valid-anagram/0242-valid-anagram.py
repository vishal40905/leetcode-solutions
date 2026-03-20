class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a = sorted(s)
        # b = sorted(t)
        # if a==b:
        #     return True
        # return False

        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
    
        