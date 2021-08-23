# Given n non-negative integers a1, a2, ..., an , where each represents
# a point at coordinate (i, ai). n vertical lines are drawn such that the
# two endpoints of the line i is at (i, ai) and (i, 0). Find two lines,
# which, together with the x-axis forms a container, such that the container
# contains the most water.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            min_height = min(height[left], height[right])
            curr_area = (right - left) * min_height
            max_water = max(max_water, curr_area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_water


height1 = [1, 1]
height2 = [4, 3, 2, 1, 4]
height3 = [1, 2, 1]

s = Solution()

print(s.maxArea(height1))
print(s.maxArea(height2))
print(s.maxArea(height3))
