class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffled_array = []

        for i in range(n):
            
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[i + n])

        return shuffled_array

# Example usage:
solution = Solution()
result = solution.shuffle([2, 5, 1, 3, 4, 7], 3)
print(result)  # Output: [2, 3, 5, 4, 1, 7]
