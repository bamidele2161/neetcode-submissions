class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for c in s:
            if c.isalnum():
                new += c.lower()
        final = new[::-1]
        if final == new:
            return True
        return False
        