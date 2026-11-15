class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        if len(nums) > 0: 
            for i in range(len(nums)):
                print(nums[i], nums[i+1], "debuggg")
                if nums[i] == nums[i+1]:
                    result = True
                else:
                    result = False
                
        return result