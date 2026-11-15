class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        result = False
        if len(nums) > 0: 
            for i in range(len(nums)-1):
                if nums[i] == nums[i-1]: #2,1,2
                    count += 1
            if count > 0:
                result = True
            else: 
                result = False
        return result