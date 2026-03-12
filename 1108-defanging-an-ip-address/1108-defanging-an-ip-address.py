class Solution:
    def defangIPaddr(self, address: str) -> str:
        len1 = len(address)
        for i in range(1,len1):
            return address.replace(".","[.]")
