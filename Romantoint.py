"""
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "IX"
Output: 9
"""



def Romantoint(str):
    values= {'I': 1 , 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum= 0
    i= 0
    while (i < len(str)):
      s1= values[str[i]]
      if (i+1 < len(str)):
        s2= values[str[i+1]]
        if (s1 >= s2):
          sum += s1
          i+=1
        else:
          sum= sum - s1
          i+=1 
      else:
        sum += s1 
        i += 1
    return sum

print(Romantoint('IX'))

"""
def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        intv = 0
        for i in range(0,len(s)):
            if(i+1 < len(s)):
                if(symbols[s[i]] < symbols[s[i+1]]):
                    intv = intv - symbols[s[i]]
                else:
                    intv = intv + symbols[s[i]]
        intv = intv + symbols[s[i]]

        return intv

"""