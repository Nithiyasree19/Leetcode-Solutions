import java.util.*;

class Solution {
    public int shortestPathBinaryMatrix(int[][] g) {
        int n = g.length;
        if (g[0][0] != 0 || g[n-1][n-1] != 0) return -1;

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0, 1});
        g[0][0] = 1;

        int[] dirs = {-1, 0, 1};

        while (!q.isEmpty()) {
            int[] p = q.poll();
            int r = p[0], c = p[1], d = p[2];
            if (r == n-1 && c == n-1) return d;

            for (int dr : dirs)
                for (int dc : dirs) {
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nc >= 0 && nr < n && nc < n && g[nr][nc] == 0) {
                        g[nr][nc] = 1;
                        q.offer(new int[]{nr, nc, d + 1});
                    }
                }
        }
        return -1;
    }
}