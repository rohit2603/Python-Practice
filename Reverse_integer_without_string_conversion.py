import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        y=x
        if(x<0):
            return False
        elif (x==0):
            return True
        else:
            count= math.floor(math.log(x,10))
            while x>0:
                x,rem=divmod(x,10)
                rev+=rem*pow(10,count)
                count-=1
            if (rev==y):
                return True
            else:
                return False
