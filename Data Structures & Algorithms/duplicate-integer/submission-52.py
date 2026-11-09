class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        result = False
        sorted_list = sorted(nums)
        if len(sorted_list) > 0: 
            for i in range(len(sorted_list)-1):
                if sorted_list[i] == sorted_list[i+1]: #2,1,2 -> 1,2,2
                    count += 1
            if count > 0:
                result = True
            else: 
                result = False
        return result