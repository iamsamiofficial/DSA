class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            l,r = i+1,len(nums)-1
            

            while l < r:
                stor = nums[i]+nums[l]+nums[r]
                if stor>0:
                    r -= 1
                elif stor<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while (nums[l] == nums[l-1] and l<r):
                        l+=1
        return res
        