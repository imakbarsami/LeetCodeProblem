class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l,r,boat=0,len(people)-1,0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            boat+=1
        return boat

obj=Solution()
print(obj.numRescueBoats([3,2,2,1],3))