class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create one set to track numbers seen in each row
        rows = [set() for _ in range(9)]
        # Create one set to track numbers seen in each column
        columns = [set() for _ in range(9)]
        # Create one set to track numbers seen in each sub-box
        sub_boxes = [set() for _ in range(9)]

        # Traverse the board
        for i in range(9):
            for j in range(9):
                # Ignore empty cells
                if board[i][j] != '.':
                    # Check for rows
                    if board[i][j] not in rows[i]:
                        # Add the number to the set
                        rows[i].add(board[i][j])
                    # Duplicate in the row
                    else:
                        return False

                    # Check for columns
                    if board[i][j] not in columns[j]:
                        # Add the number to the set
                        columns[j].add(board[i][j])
                    # Duplicate in the column
                    else:
                        return False

                    # Check the sub_box (which 3x3 box this cell belongs to)
                    # Map to sub_box index
                    box_index = (i // 3) * 3 + j // 3
                    if board[i][j] not in sub_boxes[box_index]:
                        sub_boxes[box_index].add(board[i][j])
                    # Duplicate in the 3x3 sub-box
                    else:
                        return False

        # If no duplicates were found, the board is valid
        return True