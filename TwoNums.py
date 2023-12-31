class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of elements
        num_dict = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_dict:
                # If found, return the indices of the two numbers
                return [num_dict[complement], i]
            
            # If not found, add the current number and its index to the dictionary
            num_dict[num] = i
        
        # No solution found
        return None

solution = Solution()

# Example 1:
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

# Example 2:
nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

