class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
    
        def flood(r: int, c: int):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] == newColor or image[r][c] != color:
                return 
            image[r][c] = newColor

            flood(r - 1, c)
            flood(r + 1, c)
            flood(r, c - 1)
            flood(r, c + 1)
            
        
        flood(sr, sc)
        return image
