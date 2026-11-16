class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum = 0
        while left < right:
            if sum < target:
                left = left + 1
                numbers[left] + numbers[right]
            elif sum > target:
                right = right - 1
                numbers[left] + numbers[right]
            elif sum == target:
                return [left, right]
        return []
        