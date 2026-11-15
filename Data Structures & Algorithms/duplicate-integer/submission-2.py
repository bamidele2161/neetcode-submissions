class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value = False
        for i in nums:
            print(i)
            if i == i:
                value = True
            else:
                value = False
        return value