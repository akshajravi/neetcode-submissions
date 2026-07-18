class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS,COLS = 9,9

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == ".":
                    continue
                val = board[i][j]
                if val in rows[i] or val in cols[j] or val in squares[(i//3,j//3)]:
                    return False

                cols[j].add(val)
                rows[i].add(val)
                squares[(i//3,j//3)].add(val)
        return True