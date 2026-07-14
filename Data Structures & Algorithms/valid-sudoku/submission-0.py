class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={i:set() for i in range(9)}
        cols={j:set() for j in range (9)}
        boxes={(i,j): set() for i in range(3) for j in range(3)}
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val=='.':
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)
                if val in cols[c]:
                    return False
                cols[c].add(val)
                box=(r//3,c//3)
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
        return True

        