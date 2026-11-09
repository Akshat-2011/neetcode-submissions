class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left],heights[right])
            currarea = height*width
            area = max(currarea,area)
            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1
        return area


        