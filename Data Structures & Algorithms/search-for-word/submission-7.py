class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def search(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[index] != board[row][col]:
                return False
        

            original = board[row][col]

            board[row][col] = "."

            

            result = search(row + 1, col, index + 1) or search(row - 1, col, index + 1) or search(row, col + 1, index + 1) or search(row, col - 1, index + 1)


            board[row][col] = original

            return result

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if search(r,c,0):
                       return True

        return False 
                    

                        

