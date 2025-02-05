class Solution:
    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1
        carry, res = 0, []

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            res.append(total % 10)
            i -= 1
            j -= 1
        res = res[::-1]
        res_str = ''.join(str(x) for x in res)

        return res_str



obj = Solution()
print(obj.addStrings("123", "456"))  
print(obj.addStrings("999", "1"))    
