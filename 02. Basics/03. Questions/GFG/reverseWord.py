########################################
"""You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
Example 2:

Input:
s = for
Output: rof"""
########################################


def reverseWord(s):
         revlist = list(s)
         left = 0
         right = len(s)-1
         while left < right:
             revlist[left], revlist[right] = revlist[right], revlist[left]
             left += 1
             right -= 1
         return ("".join(revlist))
print(reverseWord("Mujeeb"))