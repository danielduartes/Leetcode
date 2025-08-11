class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        vogais = []
        indice = 0
        for i in range(len(s)):
            if s[i] in "aeiou" or s[i] in "AEIOU":
                vogais.insert(0, s[i])
        for letra in s:
            if letra in "aeiou" or letra in "AEIOU":
                output += vogais[indice]
                indice += 1
            else:
                output += letra
        return output
        