class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bank = []
        for i in range(len(nums)):
            print(i)
            j = target - nums[i]
            if j in nums:
                # i is index, j is value
                position = nums.index(j)
                sub = [i, position]
                bank.append(sub)
        return bank[0]