class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        result = []
        while(i < j):
            sum = numbers[i] + numbers[j]
            if sum == target:
                result = [i + 1, j + 1]
                break
            elif sum > target:
                j -= 1
            elif  sum < target:
                i += 1
        return result 
