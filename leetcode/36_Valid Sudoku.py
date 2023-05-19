from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = []

        def checkFunction(arr):
            for b in arr:
                check = [0] * 10
                for num in b:
                    if num != ".":
                        n = int(num)
                        check[n] += 1
                        if check[n] > 1:
                            return False
            return True

        ans.append(checkFunction(board))
        ans.append(checkFunction(list(map(list, zip(*board)))))

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = [0] * 10
                for y in range(i, i + 3):
                    for x in range(j, j + 3):
                        if board[y][x] != ".":
                            n = int(board[y][x])
                            check[n] += 1
                            if check[n] > 1:
                                return False
        else:
            return all(ans)


sol = Solution()
print(
    sol.isValidSudoku(
        [
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
)
