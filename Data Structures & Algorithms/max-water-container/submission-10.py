class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        answer = 0
        while left < right:
            d = min(heights[left], heights[right])
            c = right - left
            result = c * d
            print(result)
            if answer < result:
                answer = result
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return answer





        