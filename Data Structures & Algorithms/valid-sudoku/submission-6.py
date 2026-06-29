from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = board
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for row in range(9):
            for col in range(9):
                cell_value = board[row][col]
                if cell_value=='.':
                    continue

                if cell_value in cols[col]:
                    return False


                if cell_value in rows[row]:

                    return False

                square_idx = ((row//3)+(col//3)*3)

                if cell_value in squares[square_idx] :

                    return False

                rows[row].append(cell_value)
                cols[col].append(cell_value)
                squares[square_idx].append(cell_value)

        return True
                 




