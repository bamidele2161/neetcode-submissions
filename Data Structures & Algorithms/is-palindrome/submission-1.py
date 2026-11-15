class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[0].lower() == s[-2].lower():
                return True
            return False
        