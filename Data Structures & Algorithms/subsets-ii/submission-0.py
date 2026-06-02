class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
    
        def backtrack(start, current_subset):
            results.append(list(current_subset))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop() 
        backtrack(0, [])
        return results