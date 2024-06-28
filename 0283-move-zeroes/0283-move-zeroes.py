class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pointer = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums.insert(non_zero_pointer, nums[i])
                nums.pop(i+1)
                non_zero_pointer += 1