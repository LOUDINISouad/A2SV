class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        
        for num in range(left, right + 1):
            if self.isSelfDividing(num):
                result.append(num)
        
        return result
    
    def isSelfDividing(self, num):
    
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True
