class Solution:
    def reverse(self, x: int) -> int:
        acb = 0
        if(x < 0):
            x = -x
            acb = 1
        x = str(x)
        x = reversed(x)
        x = ''.join(x)        
        x = int(x)
        
        if(x>=2147483648):
            return 0
        
        if (acb == 0):            
            return x
        else:
            x = -x
            return x
