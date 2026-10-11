### Brute Force 
```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.split()
        i = -1 
        while True:
            if temp[i]:
                return len(temp[i])
            else:
                i = i-1
```
> [!NOTE]
> ***split()*** is not required , can be done without it
> both ***time and space complexity*** is *O(n)*

### Optimized soln - 
only last word required so just use int variables 

## Key Takeaways 
- the bool value of s = "" is false but for ***s = " "*** bool value is true 
