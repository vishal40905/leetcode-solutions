class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        #here we check the char is present or not!!
        for i in s:
            if i not in freq:
                freq[i] =1
            else:
                freq[i] +=1
        #now wirttten the indices here in below code
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1




