"""
Input: s = "abcabcbb" , "pwwkew"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def LongestSubstring (seq):
    sub = {}
    cur_start= 0 # j
    i = 0 # i
    longest= 0 
   
    while cur_start < len(seq):
        if seq[cur_start] not in sub or i > sub[seq[cur_start]]:
            longest= max(longest, (cur_start - i + 1) )
            sub[seq[cur_start]] = cur_start
            
        else:
            i= sub[seq[cur_start]] + 1
            longest= max(longest, (cur_start - i + 1))
            cur_start -= 1
        cur_start += 1

           
    return longest 
    
    
print(LongestSubstring("pwwkew"))
