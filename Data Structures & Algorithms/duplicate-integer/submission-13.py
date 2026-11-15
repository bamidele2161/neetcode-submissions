class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(nums[0])
        start = nums[0]
        result = False
        for i in range(len(nums)):
            print(i)
            if start == nums[i]:
                result = True
            else:
                result = False
                
        return result