class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        j = 0

        if len(word1) >= len(word2):
            for i in range(len(word2)):
                merged_string += word1[i]
                merged_string += word2[i]
                j += 1

        if len(word2) > len(word1):
            for i in range(len(word1)):
                merged_string += word1[i]
                merged_string += word2[i]
                j += 1

        merged_string += word1[j:]
        merged_string += word2[j:]

        return merged_string