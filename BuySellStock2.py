class Solution(object):
    def maxProfit(self, prices):
        profit=0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                profit+=(prices[i]-prices[i-1])
        return profit


obj=Solution()
print(obj.maxProfit([7,6,4,3,1]))
