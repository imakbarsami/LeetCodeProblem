import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff=sys.maxsize
        ans=0
        for i in range(len(nums)):
            first=i+1
            end=len(nums)-1
            while(first<end):
                n=nums[i]+nums[first]+nums[end]
                if n==target:
                    return target
                elif (abs(n-target)<diff):
                    diff=abs(n-target)
                    ans=n
                if n>target:
                    end-=1
                else:
                    first+=1
        return ans

obj=Solution()
print(obj.threeSumClosest([-1,2,1,-4],1))