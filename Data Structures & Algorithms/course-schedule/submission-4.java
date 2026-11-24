class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, Set<Integer>> adj = new HashMap<>();

        for (int[] preq : prerequisites) {
            int a = preq[0];
            int b = preq[1];

            adj.computeIfAbsent(b, key -> new HashSet<>()).add(a);
        }

        Set<Integer> visited = new HashSet<>();
        for(int i = 0; i < numCourses; i++) {
            if (topSort(adj, i, new HashSet<>(), visited) == TopSortResult.CYCLE) {
                return false;
            }
        }
        return true;
    }

    enum TopSortResult {
        OK, CYCLE
    }

    private TopSortResult topSort(Map<Integer, Set<Integer>> graph, int node, Set<Integer> path, Set<Integer> visited) {
        if (path.contains(node)) {
            return TopSortResult.CYCLE;
        }

        if (visited.contains(node)) {
            return TopSortResult.OK;
        }

        visited.add(node);
        path.add(node);
        for (Integer neighbour : graph.getOrDefault(node, new HashSet<>())) {
            if (topSort(graph, neighbour, path, visited) == TopSortResult.CYCLE) {
                return TopSortResult.CYCLE;
            }
        }
        path.remove(node);
        return TopSortResult.OK;
    }
}
