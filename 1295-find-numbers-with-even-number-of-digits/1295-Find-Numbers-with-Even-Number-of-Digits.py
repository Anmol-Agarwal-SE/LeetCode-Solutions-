class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for n in nums:
            if (10<=n <=99) or (1000<=n <=9999) or (n==100000):
                count+=1
        return count
        