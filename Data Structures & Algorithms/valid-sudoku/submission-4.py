class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                element = board[r][c]
                box = (r // 3)*3 + (c // 3)
                if element == ".":
                    continue
                if element in rows[r] or element in cols[c] or element in boxes[box]:
                    return False
                rows[r].add(element)
                cols[c].add(element)
                boxes[box].add(element)
        return True