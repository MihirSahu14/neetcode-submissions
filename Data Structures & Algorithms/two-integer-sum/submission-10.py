class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        safe = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in safe:
                return [safe[diff], i]
            
            safe[n] = i

        