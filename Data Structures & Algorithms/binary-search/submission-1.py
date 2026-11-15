class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        for i in range(len(nums)-1):
            if target == nums[i]:
                print(i, "check")
                result = i
        return result
                
        