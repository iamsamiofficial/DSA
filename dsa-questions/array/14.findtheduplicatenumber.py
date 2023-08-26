class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = -1
        nums.sort()
        for i in range(len(nums)):
            if store == nums[i]:
                break
            else:
                store = nums[i]
        return store