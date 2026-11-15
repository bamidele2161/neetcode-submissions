class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        result = False
        if len(nums) > 0: 
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    count += 1
                else:
                    count = 0
            
            if count > 0:
                result = True
            else: 
                result = False
        return result