class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final =[]
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result < 0:
                    left += 1
                elif result > 0:
                    right -= 1
                else:
                    ans = [nums[i], nums[left], nums[right]]
                    if ans not in final:
                        final.append(ans)
                    left += 1
                    right -= 1
        return final

        

            