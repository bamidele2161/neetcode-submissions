class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bank = []
        for i in range(len(nums)):
            j = target - nums[i] 
            if j in nums and nums.index(j) != i:
                position = nums.index(j)
                sub = [i, position]
                bank.append(sub)
        return bank[0]