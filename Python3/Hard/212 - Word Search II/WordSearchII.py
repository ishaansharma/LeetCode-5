class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        row, col = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (0 > r) or (0 > c) or (r == row) or (c == col) or (r, c) in visit or board[r][c] not in node.children:
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)
            if len(res) < len(words):
                dfs(r + 1, c, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
        return list(res)
      
