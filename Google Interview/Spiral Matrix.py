"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):

    def __init__(self):
        self.ret = []

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        if matrix[0] == []:
            return []

        right = len(matrix[0]) - 1
        left = 0
        bot = len(matrix) - 1
        top = 0

        self.ret = []
        while True:

            # Right
            for i in range(left, right + 1):
                self.ret.append(matrix[top][i])
            top += 1

            if len(self.ret) == len(matrix) * len(matrix[0]):
                break

            # Down
            for i in range(top, bot + 1):
                self.ret.append(matrix[i][right])
            right -= 1

            if len(self.ret) == len(matrix) * len(matrix[0]):
                break

            # Left
            for i in range(right, left - 1, -1):
                self.ret.append(matrix[bot][i])
            bot -= 1

            if len(self.ret) == len(matrix) * len(matrix[0]):
                break

            # Up
            for i in range(bot, top - 1, -1):
                self.ret.append(matrix[i][left])
            left += 1

            if len(self.ret) == len(matrix) * len(matrix[0]):
                break

        return self.ret

mySol = Solution()
stuff = mySol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print 'suh'
