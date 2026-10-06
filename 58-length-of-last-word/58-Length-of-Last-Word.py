class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        for i in reversed(range(len(s))):
            if s[i]!=" ":
                l+=1
            elif l>0:
                return l
        return l