class Solution(object):
    def twoSum(self, nums, target):
        a=0
        for num in range(0,len(nums)):
            if a==1:
                break
            else:
                for num1 in range(num+1,len(nums)):
                    if (nums[num]+nums[num1])==target:
                        output=[num,num1]
                        return output
                        a=1
                        break