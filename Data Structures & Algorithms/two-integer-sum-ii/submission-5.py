class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        if len(numbers) == 1 and numbers[0] == target:
            ans=[target]
        else:
            for i in range(len(numbers)):
                a = numbers[i]
                b = numbers[i + 1]
                c = a + b
                
                if c == target:
                    index1 = a + 1
                    index2 = b + 1
                    ans=[index1, index2]
        return ans
        