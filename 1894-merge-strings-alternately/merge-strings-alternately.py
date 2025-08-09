class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        string_alternada = []
        for letter in word1:
            string_alternada.append(letter)
            string_alternada.append(" ")
        for letra in word2:
            if " " in string_alternada:
                i = string_alternada.index(" ")
                string_alternada[i] = letra
            else:
                string_alternada.append(letra)
        string_alternada = "".join(string_alternada)
        return string_alternada.replace(" ", "")