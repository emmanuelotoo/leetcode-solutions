class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_sum = set()
        for num in nums:
            if num in unique_sum:
                return True
            unique_sum.add(num)
        return False