class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = s.split()[::-1]
        return " ".join(output)
        