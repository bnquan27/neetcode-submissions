class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            check_set = set()
            for element in row:
                if element not in check_set:
                    check_set.add(element)
                elif element in check_set and element == ".":
                    continue
                elif element in check_set and element != ".":
                    return False
        for col in zip(*board):
            check_set = set()
            for element in col:
                if element not in check_set:
                    check_set.add(element)
                elif element in check_set and element == ".":
                    continue
                elif element in check_set and element != ".":
                    return False
        n = len(board)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                subarray = [
                    board[r][c]
                    for r in range(i, i+3)
                    for c in range(j, j+3)
                ]
                check_set = set()
                for element in subarray:
                    if element not in check_set:
                        check_set.add(element)
                    elif element in check_set and element == ".":
                        continue
                    elif element in check_set and element != ".":
                        return False
        return True
