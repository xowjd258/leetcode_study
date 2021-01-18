class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)-1):
            for j in range (i+1,len(nums)):
                if ((nums[i]+nums[j])==target):
                    return  [i,j]

target = 5
nums = [1,2,3]
sol = Solution()
sol.twoSum(nums,target)
