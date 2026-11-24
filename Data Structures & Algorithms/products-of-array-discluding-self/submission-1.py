class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        for num in nums:
            if num != 0:
               product *= num
        if 0 not in nums:
            result = [(int)(product / num) for num in nums]
        else:
            result = [0 if num != 0 else product for num in nums]
        return result