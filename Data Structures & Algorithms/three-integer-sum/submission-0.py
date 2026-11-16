class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final =[]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                         ans = [nums[i], nums[j], nums[k]]
                         new = sorted(ans)
                         if new not in final:
                            final.append(new)
        return final