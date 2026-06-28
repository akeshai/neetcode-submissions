import  numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # box_size = int(board/3)
        sudoku = np.array(board)


        blocks = []
        i = 0
        j = 0
        while i<9:
            mini_block = sudoku[i:i+3,j:j+3]
            row = mini_block.flatten()
            blocks.append(row)
            
            j+=3            
            if j==9:
                i+=3
                j = 0
                
        board = (np.concatenate((sudoku,sudoku.T,blocks)))
                
# print(blocks)
        #for square
        for row in board:
            
            duplicates = []
            for element in row:
                if element in duplicates and element!= np.str_("."):
                    print("Row checking",[element] ,"in", duplicates)
                    return False

                else:
                    duplicates.append(element)
            

      


        return True
                
        
            
            