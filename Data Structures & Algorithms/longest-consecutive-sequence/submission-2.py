#if num is the start of a sequence -> num - 1 is not in the sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        set_nums = set(nums)
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            else:
                cnt = 1
                temp = num
                while temp + 1 in set_nums:
                    cnt += 1
                    temp +=1
                if cnt > max_length:
                    max_length = cnt
        return max_length
                        
