class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = 0
        h = len(nums)-1
        while l < h:
            nums[l],nums[h] = nums[h],nums[l]
            l,h = l+1,h-1

        l = 0
        h = k-1
        while l < h:
            nums[l],nums[h] = nums[h],nums[l]
            l,h = l+1,h-1
        l = k
        h = len(nums)-1
        while l < h:
            nums[l],nums[h] = nums[h],nums[l]
            l,h = l+1,h-1
        return nums


        
