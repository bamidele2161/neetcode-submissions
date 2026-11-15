class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = False
        for i in range(len(s)-1):
            if s[0].lower() == s[-1].lower():
                result = True
            result = False
        return result
        