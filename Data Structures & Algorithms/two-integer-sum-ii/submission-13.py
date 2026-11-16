class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum = 0
        while left < right:
            if sum < target:
                left = left + 1
                sum = left+right
            elif sum > target:
                right = right - 1
                sum = left+right
            elif sum == target:
                return [left, right]
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         a = numbers[i]
        #         b = numbers[j]
        #         c = a + b
                    
        #         if c == target:
        #             index1 = i + 1
        #             index2 = j + 1
        #             return [index1, index2]
        return []
        