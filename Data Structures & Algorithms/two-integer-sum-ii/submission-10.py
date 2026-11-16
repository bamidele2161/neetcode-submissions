class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        if len(numbers) == 1 and numbers[0] == target:
            ans=[target]
        elif len(numbers) > 1:
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    a = numbers[i]
                    b = numbers[j]
                    c = a + b
                    
                    if c == target:
                        index1 = i
                        index2 = j
                        ans=[index1, index2]
        return ans
        