class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        min_num = min(nums)

        while min_num <= max_num:
            if min_num not in nums:
                return min_num
            min_num += 1
        return len(nums)