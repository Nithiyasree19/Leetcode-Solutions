import java.util.*;
class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n=quality.length;
        double[][] workers=new double[n][2];
        for (int i=0;i<n;i++) {
            workers[i][0]=(double)wage[i]/quality[i];
            workers[i][1]=quality[i];
        }
        // Sort by wage-to-quality ratio
        Arrays.sort(workers,(a,b) ->
            Double.compare(a[0],b[0])
        );
        // Max heap based on quality
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        long qualitySum=0;
        double minCost =Double.MAX_VALUE;

        for (double[] worker:workers) {

            int q=(int)worker[1];
            double ratio=worker[0];

            maxHeap.offer(q);
            qualitySum+=q;

            // Keep only k workers
            if (maxHeap.size() > k) {qualitySum -= maxHeap.poll();}

            // Calculate cost when exactly k workers remain
            if (maxHeap.size() == k) {
                double cost=qualitySum*ratio;
                minCost=Math.min(minCost, cost);
            }
        }

        return minCost;
    }
}