class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        for i in numbers:
            a = i
            b = i + 1
            c = a + b
            
            if c == target:
                index1 = numbers.index(a) + 1
                index2 = numbers.index(b) + 1
                ans=[index1, index2]
        return ans
        