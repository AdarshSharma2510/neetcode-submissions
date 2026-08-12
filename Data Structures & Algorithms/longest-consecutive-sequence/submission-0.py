class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxt = 0
        for i in range(len(nums)):
            if nums[i] - 1 in s:
                continue
            count = 1
            while nums[i] + count in s:
                count += 1
            maxt = max(maxt, count)
        return maxt