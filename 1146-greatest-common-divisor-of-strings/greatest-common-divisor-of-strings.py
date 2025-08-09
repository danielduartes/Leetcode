class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        divisor = ""
        divisores = []
        for letra in str2:
            divisor += letra
            if str1 == divisor * int(len(str1) / len(divisor)) and str2 == divisor * int(len(str2) / len(divisor)):
                divisores.append(divisor)
        if len(divisores) != 0:
            maior = max(divisores, key=len)
            return maior
        return ""