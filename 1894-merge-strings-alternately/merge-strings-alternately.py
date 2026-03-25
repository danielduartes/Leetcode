class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lista = []
        merge = ""
        lista.append(word1)
        lista.append(word2)
        for i in range(0, len(min(lista, key=len))):
            merge += word1[i]
            merge += word2[i]
        merge += max(lista, key=len)[len(min(lista, key=len))::]
        
        return merge