class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the output array with 1's
        output = [1] * n
        
        # Calculate left products and store them in output
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Calculate right products and multiply them with the left products in output
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output