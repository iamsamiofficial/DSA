class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        arr = [1]*len(nums)
        for i in range(len(nums)):
            arr[i] = pre
            pre *=nums[i]

        for i in range(len(nums)-1,-1,-1):
            arr[i] *= post
            post *= nums[i]
        return arr