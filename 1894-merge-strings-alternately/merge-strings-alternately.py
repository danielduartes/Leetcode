class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        palavras = [word1, word2]
        merged = ""

        for i in range(len(min(palavras, key=len))):
            merged += word1[i]
            merged += word2[i]
        for j in range(len(min(palavras, key=len)), len(max(palavras, key=len))):
            merged += max(palavras, key=len)[j]
        
        return merged