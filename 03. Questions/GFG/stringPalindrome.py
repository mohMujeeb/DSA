########################################
"""You are given a string s. You need to check if it is Palindrome or not.
If Palindrome return True and if not Palindrome return False

Example 1:

Input:
s = radar
Output: True 
Example 2:

Input:
s = MADAM 
Output: True"""
########################################


def reverseWord(s):
    dup = s
    revlist = list(s)
    left = 0
    right = len(s)-1
    while left < right:
        revlist[left], revlist[right] = revlist[right], revlist[left]
        left += 1
        right -= 1
    revlist = "".join(revlist)
    if revlist == dup:
        return True
    else:
        return False  
      
print(reverseWord("radar"))