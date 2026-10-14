class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique=list(set(nums))
        unique.sort()
        if len(unique)<3:
            return unique[-1]
        return unique[-3]