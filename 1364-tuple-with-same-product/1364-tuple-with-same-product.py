class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums_length = len(nums)
        pair_products_frequency = {}
        total_number_of_tuples = 0
        # Iterate through each pair of numbers in `nums`
        for first_index in range(nums_length):
            for second_index in range(first_index + 1, nums_length):
                # Increment the frequency of the product of the current pair
                product_value = nums[first_index] * nums[second_index]
                if product_value in pair_products_frequency:
                    pair_products_frequency[product_value] += 1
                else:
                    pair_products_frequency[product_value] = 1
        for product_frequency in pair_products_frequency.values():
            #nc2
            pairs_of_equal_product = (
                (product_frequency - 1) * product_frequency // 2
            )
            total_number_of_tuples += 8 * pairs_of_equal_product
        return total_number_of_tuples