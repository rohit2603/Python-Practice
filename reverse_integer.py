class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        Rev=(-1 if x<0 else 1)*int(str(x)[::-1].replace("-",""))
        if (Rev>pow(2,31)-1 or Rev<-1*pow(2,31)):
            return 0
        else:
            return Rev
