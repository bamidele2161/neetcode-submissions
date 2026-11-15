class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if i == i:
                return True
            else:
                return False
        