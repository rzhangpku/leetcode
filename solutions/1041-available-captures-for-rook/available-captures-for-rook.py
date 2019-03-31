# -*- coding:utf-8 -*-


# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.
#
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.
#
# Return the number of pawns the rook can capture in one move.
#
#  
#
# Example 1:
#
#
#
#
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# In this example the rook is able to capture all the pawns.
#
#
# Example 2:
#
#
#
#
# Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation: 
# Bishops are blocking the rook to capture any pawn.
#
#
# Example 3:
#
#
#
#
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# The rook can capture the pawns at positions b5, d6 and f5.
#
#
#  
#
# Note:
#
#
# 	board.length == board[i].length == 8
# 	board[i][j] is either 'R', '.', 'B', or 'p'
# 	There is exactly one cell with board[i][j] == 'R'
#
#


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        r=0
        m=len(board)
        n=len(board[0])
        flag=0
        for i in range(m):
            if flag==1:
                break
            for j in range(n):
                if str(board[i][j])=="R":
                    ri=i
                    rj=j
                    flag=1
                    break
        for k in range(ri+1,m):
            if board[k][rj]=="p":
                r+=1
                break
            if board[k][rj]=="B":
                break
        for k in range(ri-1,-1,-1):
            if board[k][rj]=="p":
                r+=1
                break
            if board[k][rj]=="B":
                break
        for k in range(rj+1,n):
            if board[ri][k]=="p":
                r+=1
                break
            if board[ri][k]=="B":
                break
        for k in range(rj-1,-1,-1):
            if board[ri][k]=="p":
                r+=1
                break
            if board[ri][k]=="B":
                break
        return r
