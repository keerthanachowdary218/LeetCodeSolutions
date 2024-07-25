class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])
            return merge(left_half, right_half)

        def merge(left, right):
            sorted_list = []
            i = j = 0
            # Merge the two lists together while maintaining order
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            # If there are remaining elements in the left list, add them to the sorted list
            while i < len(left):
                sorted_list.append(left[i])
                i += 1
            # If there are remaining elements in the right list, add them to the sorted list
            while j < len(right):
                sorted_list.append(right[j])
                j += 1
            return sorted_list
        sorted_arr = merge_sort(nums)
        return sorted_arr
        
