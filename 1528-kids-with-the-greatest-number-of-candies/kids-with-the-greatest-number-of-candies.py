class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        maior_numero = max(candies)
        for number in candies:
            if number + extraCandies >= maior_numero:
                output.append(True)
            else:
                output.append(False)

        return output
        