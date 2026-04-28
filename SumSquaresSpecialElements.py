class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        n = len(nums)

        cond = []
        sums = 0
        
        for i in range(1,n+1):
            if n % i == 0:
                cond.append(nums[i-1])
        
        for j in cond:
            sums += j * j
        
        return sums
