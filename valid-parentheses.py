class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a stack to keep track of open brackets
        stack = []
        
        # Define a mapping of open and close brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_mapping:
                # Pop the top element from the stack if it's not empty; otherwise, assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding open bracket
                if bracket_mapping[char] != top_element:
                    return False
            else:
                # If the character is an open bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all open brackets have been closed in the correct order
        return not stack

