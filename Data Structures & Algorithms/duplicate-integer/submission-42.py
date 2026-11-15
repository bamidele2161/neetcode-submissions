class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        result = False
        if len(nums) > 0: 
            for i in range(len(nums)-1):
                print(nums[i], nums[i+1], "checking")
                if nums[i] == nums[i+1]:
                    count += 1
                else:
                    count = 0
            
            if count > 0:
                print(count, "count")
                result = True
            else: 
                print(count, "count")
                result = False
        return result