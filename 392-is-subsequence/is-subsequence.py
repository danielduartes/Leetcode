class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        resposta = ""
        contador = 0
        for i in range(len(s)):
            for j in range(contador, len(t)):
                contador += 1
                if s[i] == t[j]:
                    resposta += s[i]
                    break
        if resposta == s:
            return True
        return False     