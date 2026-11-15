class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum = 0
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left = left + 1
                sum = numbers[left] + numbers[right]
            elif sum > target:
                right = right - 1
                sum = numbers[left] + numbers[right]
            elif sum == target:
                return [left + 1, right + 1]
        return []
        