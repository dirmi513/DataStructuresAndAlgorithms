from typing import List


class QuickSelect: 
    
    @staticmethod
    def quick_select(
        nums: List[int],
        kth_smallest: int,
    ) -> List[int]:
        return QuickSelect.split(0, len(nums)-1, nums, kth_smallest)
    
    @staticmethod
    def split(
        left: int, 
        right: int, 
        nums: List[int], 
        kth_smallest: int
    ) -> List[int]:
        if left >= right:
            return nums
        
        pivot = QuickSelect.partition(left, right, nums)
        if pivot == kth_smallest:
            return nums
        elif pivot < kth_smallest:
            QuickSelect.split(pivot+1, right, nums, kth_smallest)
        else:
            QuickSelect.split(left, pivot-1, nums, kth_smallest)
        
        return nums
    
    @staticmethod
    def partition(
        left: int, 
        right: int, 
        nums: List[int]
    ) -> int:
        pivot = nums[left]
        original_left = left
        original_right = None
        left += 1
        
        while True:
            while left < right and nums[left] < pivot:
                left += 1
            
            while left <= right and nums[right] >= pivot:
                right -= 1
            
            if left >= right:
                break
                
            nums_right = nums[right]
            nums[right] = nums[left]
            nums[left] = nums_right
        
        nums_right = nums[right]
        nums[right] = nums[original_left]
        nums[original_left] = nums_right
        
        return right


# want Kth smallest element
unsorted_array = [10, 43, 2, 5, 24, 8, 4]
k = 5
quick_select_arr = QuickSelect.quick_select(unsorted_array, k)
print(unsorted_array,
      quick_select_arr,
      f'{k}th smallest element: {quick_select_arr[k-1]}',
      sep='\n'
      )
