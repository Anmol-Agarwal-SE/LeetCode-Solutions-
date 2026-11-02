class Solution(object):
    def shipWithinDays(self, weights, days):
        def can_ship(cap):
            d = 1
            cur = 0

            for w in weights:
                if cur + w > cap:
                    d += 1
                    cur = 0
                cur += w

            return d <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left