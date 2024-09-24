class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        while (k != 0):
            x = nums[-1]
            nums.insert(0, x)
            nums.pop(-1)
            k = k - 1