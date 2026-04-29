class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_elements = {}
        for index, value in enumerate(nums):
            target_minus_value = target - value
            if target_minus_value in seen_elements:
                index_array = []
                index_array.append(seen_elements[target_minus_value])
                index_array.append(index)
                return index_array 
            seen_elements[value] = index