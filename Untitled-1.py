class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        a=[i,j]
                        return a
nums= [2,7,11,15]
target = 9
a=Solution()                
a.twoSum(nums,target)
        