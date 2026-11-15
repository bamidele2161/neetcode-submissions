class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        if len(nums) > 0: 
            for i in nums:
                print(i, i+1, "debuggg")
                if i == i+1:
                    result = True
                else:
                    result = False
                
        return result