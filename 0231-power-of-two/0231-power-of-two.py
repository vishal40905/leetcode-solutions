class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     using loop
    #     while n%2 == 0:
    #         n=n//2
    #     return n==
        def isPowerOfTwo(self, n: int) -> bool:
            #Base Case
            if n<=0:
                return False
            if n == 1:
                return True
            if n%2!=0:
                return False
                #Recusrive Case
            return self.isPowerOfTwo(n//2)

        