class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max = curr_min = 1

        for num in nums:
            temp = curr_max * num
            curr_max = max(temp, curr_min * num, num)
            curr_min = min(temp, curr_min * num, num)

            res = max(res, curr_max)
        
        return res