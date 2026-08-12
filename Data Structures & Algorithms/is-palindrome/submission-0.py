class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum():
                a = c.lower()
                string += a
        return string == string[::-1]