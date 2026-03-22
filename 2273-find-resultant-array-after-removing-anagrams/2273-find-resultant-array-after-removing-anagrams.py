class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        freq = []
        for i in words:
            if not freq or sorted(i) != sorted(freq[-1]):
                freq.append(i)
        return freq


        