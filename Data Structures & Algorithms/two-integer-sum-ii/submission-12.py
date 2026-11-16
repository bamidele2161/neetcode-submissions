class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                a = numbers[i]
                b = numbers[j]
                c = a + b
                    
                if c == target:
                    index1 = i + 1
                    index2 = j + 1
                    return [index1, index2]
        return []
        