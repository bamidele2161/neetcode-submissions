class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        for i in range(0, len(nums)):
            if target == nums[i]:
                result = i
        return result
                
        