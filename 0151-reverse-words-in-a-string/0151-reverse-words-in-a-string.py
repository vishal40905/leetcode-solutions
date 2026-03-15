class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        # s = s.split()

        # s.reverse()

        # return " ".join(s)
     #we can  write also in this way!!
        return " ".join(reversed(s.strip().split()))