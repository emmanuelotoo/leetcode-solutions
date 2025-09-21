class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the majority element is always the number in the middle so let me sort it 
        return sorted(nums)[len(nums) // 2]