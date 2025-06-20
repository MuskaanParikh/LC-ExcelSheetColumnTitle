import math

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        while columnNumber > 0: 
            columnNumber -= 1
            result = ALPHABET[columnNumber % 26] + result
            columnNumber = math.floor(columnNumber/26)
        return result