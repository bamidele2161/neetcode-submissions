class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        for i in numbers:
            a = i
            b = i + 1
            c = a + b
            if c == target:
                ans=[a, b]
        return ans
        