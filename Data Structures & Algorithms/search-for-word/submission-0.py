class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(row,col,word_index):
            #base cases
            if word_index == len(word):
                return True
            
            if (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0])) or (board[row][col]!= word[word_index]):
                return False

            original = board[row][col]

            board[row][col] = '.'

            result = (backtrack(row+1, col, word_index+1) or
              backtrack(row-1, col, word_index+1) or
              backtrack(row, col+1, word_index+1) or
              backtrack(row, col-1, word_index+1))
            
            board[row][col] = original

            return result


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True
        return False
            

    