class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(numbers)-1):
            a = numbers[i]
            b = numbers[i + 1]
            c = a + b
            
            if c == target:
                index1 = a
                index2 = b
                print(index1, index2, "checking")
                ans=[index1, index2]
        return ans
        