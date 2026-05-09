class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        second_array = []

        for num in nums:
            second_array.append(num)
        return second_array + nums