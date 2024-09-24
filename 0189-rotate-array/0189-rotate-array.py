class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        nums2 = nums.copy()
        
        for i in range(n):
            nums[(i + k) % n] = nums2[i]