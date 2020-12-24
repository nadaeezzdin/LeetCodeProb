"""
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range:[−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def ReverseNum(num):
    sign= -1 if num < 0 else 1
    snum= num * sign
    while snum :
        if snum % 10 == 0:
           snum //= 10
        else:
            break
    
    snum= str(snum)
    reversednum=snum[::-1]
    reversednum=int(reversednum)
    #-2147483648  2147483647
    if -2147483648 <= reversednum <= 2147483647:
        return sign*reversednum
    else:
        return 0
    
 
    

print(ReverseNum(1534236469))
     