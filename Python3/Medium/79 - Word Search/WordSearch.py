class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r >= row or c >= col or r < 0 or c < 0 or (r, c) in visited or word[i] != board[r][c]:
                return False
            visited.add((r, c))
            res = dfs(i + 1, r + 1, c) or dfs(i + 1, r - 1, c) or dfs(i + 1, r, c + 1) or dfs(i + 1, r, c - 1)
            visited.remove((r, c))
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(0, r, c):
                    return True
        return False
      
