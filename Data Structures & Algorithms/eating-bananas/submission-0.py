class Solution:
    def time(self, piles, taken, h):
        result = 0
        for pile in piles:
            result += (pile + taken - 1) // taken
        return result

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            time = self.time(piles, mid, h)
            if time <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l