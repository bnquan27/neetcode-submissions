#Naive solution O(n^2) in time and O(n) space complexity
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not check_element(row):
                return False
        for col in zip(*board):
            if not check_element(col):
                return False
        n = len(board)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                subarray = [
                    board[r][c]
                    for r in range(i, i+3)
                    for c in range(j, j+3)
                ]
                if not check_element(subarray):
                    return False
        return True
def check_element(array):
    check_set = set()

    for element in array:
        if element == ".":
            continue

        if element in check_set:
            return False

        check_set.add(element)

    return True