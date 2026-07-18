class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #VALIDATING ROWS
        #looping through all the rows of boards
        for i in range(len(board)):
            #loop through each index of each row
            seen = set()
            for j in range(len(board[i])):
                current = board[i][j]
                if (current != "."):
                    if current not in seen:
                        seen.add(current)
                    else:
                        return False
                else:
                    continue
                
        #VALIDATING COLUMNS
        num_cols = len(board[0])
        num_rows = len(board)
        for i in range(num_cols):
            seen = set()
            for j in range(num_rows):
                current = board[j][i] 
                if current != ".":
                    if current not in seen:
                        seen.add(current)
                    else: return False;
                else:
                    continue
        
        #VALIDATING 3X3 SQUARES
        num_rows = len(board)
        num_cols = len(board[0])
        map = {}
        for i in range(9):
            map[i] = set()

        for i in range(num_rows):
            for j in range(num_cols):
                current = board[i][j]
                index = (i // 3) * 3 + (j // 3)
                if current != ".":
                    if(current not in map[index]):
                        map[index].add(current)
                    else:
                        return False;
                else:
                    continue
                    
        return True


                


                    
