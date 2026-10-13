class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=0
        for i in range(len(accounts)):
            cw=sum(accounts[i])
            if cw>m:
                m=cw
        return m