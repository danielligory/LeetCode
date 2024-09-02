class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join([str(i) for i in digits])
        number = int(string) + 1
        digits_list = [int(digit) for digit in str(number)]
        return digits_list
        