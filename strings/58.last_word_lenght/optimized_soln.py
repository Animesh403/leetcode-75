class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        count = 0
        while i>=-len(s):# >= , equality is needed so as to check one character lenght string eg 'a'. 
            if s[i]!=" ":
                count += 1
                i -= 1
            elif (s[i]==" " and count == 0):
                i -= 1
            else:
                break
        return count
