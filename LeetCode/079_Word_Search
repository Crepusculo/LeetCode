# -*- coding: UTF-8 -*-
# http://www.cnblogs.com/chruny/p/5088549.html
# a little stupid

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        row_beg = 0
        row_end = len(board[0])
        clm_beg = 0
        clm_end = len(board)
        l = len(word)
        if len == 0:
            return False
        if clm_end == 0:
            return False
        visit = [[False for i in range(row_end)] for j in range(clm_end)]

        def dfs(x, y, word):
            if len(word) == 0:
                return True
            if x > row_beg and not visit[x-1][y] and board[x - 1][y] == word[0]:
                visit[x - 1][y] = True
                if dfs(x - 1, y, word[1:]):
                    return True
                visit[x - 1][y] = False
            if y > clm_beg and not visit[x][y-1] and board[x][y-1] == word[0]:
                visit[x][y-1] = True
                if dfs(x, y-1, word[1:]):
                    return True
                visit[x][y-1] = False
            if x + 1 < clm_end and not visit[x+1][y] and board[x+1][y] == word[0]:
                visit[x+1][y] = True
                if dfs(x+1 ,y, word[1:]):
                    return True
                visit[x+1][y] = False
            if y + 1 < row_end and not visit[x][y + 1] and board[x][y + 1] == word[0]:
                visit[x][y + 1] = True
                if dfs(x, y + 1, word[1:]):
                    return True
                visit[x][y + 1] = False
            return False
        for i in range(clm_end):
            for j in range(row_end):
                if board[i][j] == word[0]:
                    visit[i][j] = True
                    if dfs(i, j ,word[1:]):
                        return True
                    visit[i][j] = False
        return False


def main():
    board_list = \
        [
            [
                ['F', 'X', 'E'],
                ['A', 'U', 'E'],
                ['S', 'F', 'F']
            ],
            [
                ['F', 'U', 'S', 'O'],
                ['A', 'B', 'C', 'D'],
                ['S', 'F', 'E', 'F']
            ],
            ["aa"],
            ["ab", "cd"]
        ]


if __name__ == '__main__':
    main()
