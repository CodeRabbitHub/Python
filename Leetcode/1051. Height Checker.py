class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected_heights[i]:
                count += 1
        return count
