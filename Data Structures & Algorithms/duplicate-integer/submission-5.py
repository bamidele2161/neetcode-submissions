class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        for i in nums:
            print(i)
            if int(i) != int(i):
                result = True
            else:
                result = False
        print('valuu', result)
        return result