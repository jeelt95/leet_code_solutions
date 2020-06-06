import numpy as np
from typing import List

class Solution:
    def getFirstRow(self, xi, yi, xe, ye, matrix):
        res = []
        for y in range(yi, ye+1):
            if(matrix[xi][y] != None):
                res.append(matrix[xi][y])
                matrix[xi][y] = None
        xi += 1
        return (res, xi, yi, xe, ye)
    
    def getLastCol(self, xi, yi, xe, ye, matrix):
        res = []
        for x in range(xi, xe+1):
            if(matrix[x][ye] != None):
                res.append(matrix[x][ye])
                matrix[x][ye] = None
        ye -= 1
        return (res, xi, yi, xe, ye)
    
    def getLastRow(self, xi, yi, xe, ye, matrix):
        res = []
        for y in range(ye, yi-1, -1):
            if(matrix[xe][y] != None):
                res.append(matrix[xe][y])
                matrix[xe][y] = None
        xe -= 1
        return (res, xi, yi, xe, ye)
    
    def getFirstCol(self, xi, yi, xe, ye, matrix):
        res = []
        for x in range(xe, xi-1, -1):
            if(matrix[x][yi] != None):
                res.append(matrix[x][yi])
                matrix[x][yi] = None
        yi += 1
        return (res, xi, yi, xe, ye)
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xi = 0
        yi = 0
        if(len(matrix)>0):
            xe = len(matrix)-1
            ye = len(matrix[0])-1
        else:
            return []
        res = []
        curr_res = []
        while(xi <= xe and yi <= ye):
            curr_res, xi, yi, xe, ye = self.getFirstRow(xi, yi, xe, ye, matrix)
            res.extend(curr_res)
            curr_res, xi, yi, xe, ye = self.getLastCol(xi, yi, xe, ye, matrix)
            res.extend(curr_res)
            curr_res, xi, yi, xe, ye = self.getLastRow(xi, yi, xe, ye, matrix)
            res.extend(curr_res)
            curr_res, xi, yi, xe, ye = self.getFirstCol(xi, yi, xe, ye, matrix)
            res.extend(curr_res)
        return res

s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(s.spiralOrder(matrix))