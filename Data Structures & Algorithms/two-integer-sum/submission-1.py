class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in maps:
                return [maps[comp], i]
            maps[num] = i
        return [-1, -1]