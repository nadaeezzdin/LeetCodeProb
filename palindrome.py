"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.
solve it without converting the integer to a string
"""
def PalindromeNum(num):
    sign= -1 if num < 0 else 1
    snum= num * sign
    reversedNum= 0
    while snum :
        reminder= snum % 10
        reversedNum = (reversedNum * 10) + reminder
        snum = snum // 10
    if num == reversedNum:
        return True
    else:
        return False
    
        
print(PalindromeNum(1001))