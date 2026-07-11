class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noduplicate = set()
        for num in nums:
            if num in noduplicate:
                return True
            noduplicate.add(num)
        return False
