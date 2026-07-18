class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def search(row,col,word_index):
            #base cases
            if word_index == len(word):
                return True
            
            if (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0])) or (board[row][col]!= word[word_index]):
                return False

            original = board[row][col]

            board[row][col] = '.'

            result = (search(row+1, col, word_index+1) or
              search(row-1, col, word_index+1) or
              search(row, col+1, word_index+1) or
              search(row, col-1, word_index+1))
            
            #this is where we backtrack by reverting the board
            board[row][col] = original

            return result


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i,j,0):
                        return True
        return False
            

    