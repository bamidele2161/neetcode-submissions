class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        result = False
        for i in nums:
            print(i)
            if i == i:
                count += 1
                result = True
            else:
                count = 0
                result = False
        return count, result