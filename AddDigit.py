class Solution(object):
    def addDigits(self, num):
        if num==0:
            return 0
        else:
            return num%9 if num%9!=0 else 9
obj=Solution()
print(obj.addDigits(14))    
