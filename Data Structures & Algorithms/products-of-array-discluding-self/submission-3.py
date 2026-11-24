#Solution without division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        suffix_prod = [1] * (len(nums))
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        i = len(nums) - 2
        while(i >= 0):
            suffix_prod[i] = nums[i+1] * suffix_prod[i+1]
            i -= 1
        for i in range(len(nums)):
            output[i] = output[i] * suffix_prod[i]
        return output