class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        l = 0
        count = 0
        for r in range(len(s)):
            c = s[r]
            while c in sets:
                sets.remove(s[l])
                l += 1
            sets.add(c)
            count = max(count, r - l + 1)
        return count