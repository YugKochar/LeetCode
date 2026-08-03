class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        if dividend == 2**31 and divisor == 1:
            return 2**31 -1
        if divisor == 1:
            return dividend

        isPositive = True
        if dividend>=0 and divisor < 0:
            isPositive = False
        elif dividend < 0 and divisor >0:
            isPositive = False
        n = abs(dividend)
        d = abs(divisor)
        ans = 0
        sum = 0
        while sum +d <=n:
            temp = d
            count = 1
            while sum+(temp<<1)<=n:
                temp <<=1
                count <<=1
            sum+=temp
            ans += count

        if ans > 2**31 -1  and isPositive:
            return 2**31 -1
        if ans > 2**31 -1 and not isPositive:
            return -2**31
        return ans if isPositive else -ans