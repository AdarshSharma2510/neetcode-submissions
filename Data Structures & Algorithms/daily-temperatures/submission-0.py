class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                diff = i - stack[-1][1] 
                result[stack[-1][1]] = diff
                stack.pop()
            stack.append([temp, i])
        return result