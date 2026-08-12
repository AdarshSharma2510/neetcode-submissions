class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxt = 0
        while l < r:
            h = min(heights[l], heights[r])
            water = h * (r - l )
            maxt = max(maxt, water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxt