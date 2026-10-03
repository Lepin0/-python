class Solution:
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])
        
        output = [[0] * n for _ in range(m)]
        
        def smooth(r, c):
            total_sum = 0
            count = 0
            
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < m and 0 <= nc < n:
                        total_sum += img[nr][nc]
                        count += 1
                        
            return total_sum // count

        for i in range(m):
            for j in range(n):
                output[i][j] = smooth(i, j)
                
        return output