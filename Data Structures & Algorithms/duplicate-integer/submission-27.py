class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        if len(nums) > 0: 
            for i in nums:
                print(i)
                if i == i+1:
                    print(i, i+1, "debuggg")
                    result = True
                else:
                    result = False
                
        return result