class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bank = []
        final = []
        for i in range(len(nums)):
            j = target - nums[i] 
            if j in nums and nums.index(j) != i:
                position = nums.index(j)
                print(position, i , "gggg")
                sub = [position, i]
                bank.append(sub)

        #bank = [[1,0],[0,1]] start is less than end
        for i in bank:
            start = i[0]
            end = i[1]
            if start < end:
                final = i
        return final