class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            triangulo = [[1]]
        elif numRows == 2:
            triangulo = [[1],[1,1]]
        elif numRows > 2:
            triangulo = [[1],[1,1]]
            for i in range(numRows):
                linha = [1]
                if i > 1:
                    for j in range(len(triangulo[-1])-1):
                        novo_numero = triangulo[-1][j] + triangulo[-1][j+1]
                        linha.append(novo_numero)
                    linha.append(1)
                    triangulo.append(linha)
                
        return triangulo