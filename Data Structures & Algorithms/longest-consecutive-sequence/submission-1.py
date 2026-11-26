#if num is the start of a sequence -> num - 1 is not in the sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        set_nums = set()
        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
            else:
                continue
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            else:
                seq = set()
                seq.add(num)
                temp = num
                while temp + 1 in set_nums:
                    seq.add(temp + 1)
                    temp +=1
                if len(seq) > max:
                    max = len(seq)
        return max
                        
