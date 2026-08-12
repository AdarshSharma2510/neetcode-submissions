class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = [0] * n
        r = [0] * n

        maxl = 0
        maxr = 0

        for i in range(n):
            l[i] = maxl
            maxl = max(maxl, height[i])
        for i in range(n - 1, -1, -1):
            r[i] = maxr
            maxr = max(maxr, height[i])
        result = 0
        for i in range(n):
            result += max(0, min(l[i], r[i]) - height[i])
        return result