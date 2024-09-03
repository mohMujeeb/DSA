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