class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def rob_linear(houses: List[int]) -> int:
            prev2 = houses[0]
            prev1 = max(houses[0], houses[1])
            
            for i in range(2, len(houses)):
                current = max(prev1, prev2 + houses[i])
                prev2, prev1 = prev1, current
            
            return prev1
        
        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )

        