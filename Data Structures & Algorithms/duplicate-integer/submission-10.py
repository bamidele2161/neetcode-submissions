class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        start = nums[0]
        result = False
        for i in nums:
            print(i)
            if start == i:
                result = True
            else:
                result = False
                
        return result