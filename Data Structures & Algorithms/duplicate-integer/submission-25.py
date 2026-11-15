class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        if len(nums) > 0: 
            print(nums[0], "checking")
            start = nums[0]
            for i in range(len(nums)):
                print(i)
                if start == nums[i]:
                    result = True
                else:
                    result = False
                
        return result