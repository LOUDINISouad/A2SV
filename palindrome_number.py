class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Check if the number is negative
        if x < 0:
            return False

        # Convert the number to a string
        x_str = str(x)

        # Reverse the string
        reversed_x_str = x_str[::-1]

        # Compare the original string with the reversed string
        return x_str == reversed_x_str

