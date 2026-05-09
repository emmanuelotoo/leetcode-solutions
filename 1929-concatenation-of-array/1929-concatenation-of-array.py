class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums * 2 simple one liner
        second_array = []

        for num in nums:
            second_array.append(num)
        return second_array + nums