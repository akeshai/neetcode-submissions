import  numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # box_size = int(board/3)
        i = 0
        j = 0
        k = 0
        #for square
        board = np.array(board)
        for row in board:
            
            duplicates = []
            for element in row:
                if element in duplicates and element!= np.str_("."):
                    print("Row checking",[element] ,"in", duplicates)
                    return False

                else:
                    duplicates.append(element)
            

        
        for col in board.T:
            duplicates = []
            for element in col:
                if element in duplicates and element!= np.str_("."):
                    print("col checking",[element] ,"in", duplicates)

                    return False
                else:
                    duplicates.append(element)
            
        
 
        while i<9:
            mini_block = board[i:i+3,j:j+3]
            row = mini_block.flatten()
            duplicates = []
            for element in row:
                if element in duplicates and element!= np.str_("."):
                    print("block checking",[element] ,"in", duplicates)

                    return False
                else:
                    duplicates.append(element)
            
            j+=3            
            if j==9:
                i+=3
                j = 0



        return True
                
        
            
            