class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = False
        sorted_first = sorted(s)
        sorted_sec = sorted(t)
        if sorted_first == sorted_sec:
            result = True
        else: 
            result = False
        
        return result