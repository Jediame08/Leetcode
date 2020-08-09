class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        
        for i,val in enumerate(nums):
            complement = target - val
            if complement in maps:
                return [maps[complement], i]
            maps[val] = i
        
        return []
