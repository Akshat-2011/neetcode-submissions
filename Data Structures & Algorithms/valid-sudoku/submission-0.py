from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        tri_set = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_set[i]:
                        return False
                    if board[i][j] in col_set[j]:
                        return False
                    if board[i][j] in tri_set[(i//3,j//3)]:
                        return False
                    else:
                        row_set[i].add(board[i][j])
                        col_set[j].add(board[i][j])
                        tri_set[(i//3,j//3)].add(board[i][j])
        return True
                
                    
