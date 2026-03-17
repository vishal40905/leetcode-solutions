class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n =len(nums)
        dict1 = {}
        for i in range(n):
            reminder = target - nums[i]
            if reminder in dict1:
                return [dict1[reminder],i]
            dict1[nums[i]]=i

            