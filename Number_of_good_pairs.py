class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        num_freq = {}

        for num in nums:
            if num in num_freq:
                count += num_freq[num]
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        return count

# Example usage:
solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # Output: 4
print(solution.numIdenticalPairs([1, 1, 1, 1]))        # Output: 6
print(solution.numIdenticalPairs([1, 2, 3]))           # Output: 0
"""The aim of the "Number of Good Pairs" problem is to count the number of pairs of indices (i, j) in an array, where the elements at those indices are equal (`nums[i] == nums[j]`) and the index `i` is strictly less than `j`. These pairs are referred to as "good pairs." The goal is to determine and return the count of such good pairs in the given array."""