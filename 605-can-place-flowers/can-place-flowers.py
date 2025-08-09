class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        new_flowers = 0
        old_flowerbed = list(flowerbed)

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0:
                    if len(flowerbed) != 1:
                        if flowerbed[i + 1] == 0:
                            flowerbed[i] = 1
                    else:
                        flowerbed[i] = 1
                elif 0 < i < len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        
        for j in range(len(old_flowerbed)):
            if old_flowerbed[j] != flowerbed[j]:
                new_flowers += 1
                
        if n <= new_flowers:
            return True

        else:
            return False
        