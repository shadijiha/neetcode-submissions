class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::unordered_map<int, std::unordered_set<int>> adj;

        for(auto& preq : prerequisites) {
            int a = preq[0];
            int b = preq[1];

            adj[b].insert(a);
        }

        std::unordered_set<int> visited;

        for (int i = 0; i < numCourses; i++) {
            std::unordered_set<int> path;
            if (topSort(adj, i, path, visited) != TopSortResult::Ok) {
                return false;
            }
        }

        return true;
    }

    enum class TopSortResult {
        Cycle = 0, Ok = 1 
    };

private:
    TopSortResult topSort(const std::unordered_map<int, std::unordered_set<int>>& graph, int node, std::unordered_set<int>& path, std::unordered_set<int>& visited) {

        if (path.find(node) != path.end()) {
            return TopSortResult::Cycle;
        }

        if (visited.find(node) != visited.end()) {
            return TopSortResult::Ok;
        } 
        visited.insert(node);

        if (graph.find(node) == graph.end()) {
            return TopSortResult::Ok;
        }

        path.insert(node); 

        for(int neighbour : graph.at(node)) {
            if (topSort(graph, neighbour, path, visited) == TopSortResult::Cycle) {
                return TopSortResult::Cycle;
            }
        }

        path.erase(node);

        return TopSortResult::Ok;
    }
};
