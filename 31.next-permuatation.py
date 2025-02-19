class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        k = - 1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i-1]:
                k = i
                break

        # if not found k
        if k == -1:
            nums.reverse()
            return
        
        l = n-1
        while l > k and nums[l] <= nums[k]:
            l -= 1

        nums[k], nums[l] = nums[l], nums[k]
        
        lo, hi = k+1, n-1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo + 1, hi - 1
