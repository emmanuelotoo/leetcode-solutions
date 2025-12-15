class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if nums in set
        #   return true:
        #       else:
        #       set.add(num)
        #           return false
        unique_num = set()
        for num in nums:
            if num in unique_num:
                return True
            unique_num.add(num)
        return False