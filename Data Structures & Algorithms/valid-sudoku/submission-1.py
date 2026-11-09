from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_rows = defaultdict(set)
        set_cols = defaultdict(set)
        set_3 = defaultdict(set)
        for i in range(9):
            for j in range(9):
                curr_val = board[i][j]
                if curr_val == '.':
                    continue
                if (curr_val in set_rows[i]) or (curr_val in set_cols[j]) or (curr_val in set_3[(i//3, j//3)]):
                    return False
                set_rows[i].add(curr_val)
                set_cols[j].add(curr_val)
                set_3[(i//3,j//3)].add(curr_val)
        return True
                

        
                
                    
