class Solution(object):
    def maxProfit(self, prices):
        current=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]<current:
                current=prices[i]
            else:
                maxprofit=max(maxprofit,(prices[i]-current))
        return maxprofit
    
obj=Solution()
print(obj.maxProfit([7,6,4,3,1]))