class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        palavras = [word1, word2]
        merged = ""

        for i in range(len(min(palavras, key=len))):
            merged += word1[i]
            merged += word2[i]
        for j in range(len(min(palavras, key=len)), len(max(palavras, key=len))):
            merged += max(palavras, key=len)[j]
        
        return merged