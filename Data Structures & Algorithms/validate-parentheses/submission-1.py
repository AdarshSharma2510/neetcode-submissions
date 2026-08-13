class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {']' : '[', '}': '{', ')' : '('}
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == maps[c]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True