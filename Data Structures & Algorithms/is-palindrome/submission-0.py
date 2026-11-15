class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s[0].lower() == s[-2].lower():
            return True
        return False
        