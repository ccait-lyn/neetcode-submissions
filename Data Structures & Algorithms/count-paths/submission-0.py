class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sol = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            sol[0][j] = 1
        
        for i in range(m):
            sol[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                sol[i][j] = sol[i][j-1] + sol[i-1][j]

        return sol[m-1][n-1]