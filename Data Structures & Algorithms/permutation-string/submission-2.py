class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t1 = Counter(s1)
        n1 = len(s1)
        for i in range(len(s2) - n1 + 1):
            c1 = Counter(s2[i : i + n1])
            if t1 == c1:
                return True
        return False