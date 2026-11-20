class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int ROWS = heights.size();
        int COLS = heights[0].size();

        // (effort, pointx, pointy)
        using State = std::tuple<int, int, int>;

        std::priority_queue<State, std::vector<State>, std::greater<State>> q;
        q.push({0, 0, 0});

        std::vector<bool> visited(ROWS * COLS, false);

        while(!q.empty())  {
            State node = q.top();
            q.pop();
            auto [effort, y, x] = node;

            if (y == ROWS - 1 && x == COLS - 1) {
                // reached
                return effort;
            }

            if (visited[y * COLS + x]) {
                continue;
            }
            visited[y * COLS + x] = true;

            constexpr std::array<std::pair<int, int>, 4> directions = {
                std::pair{0, 1}, std::pair{0, -1}, std::pair{1, 0}, std::pair{-1, 0}
            };

            for(auto [dy, dx] : directions) {
                int next_y = dy + y;
                int next_x = dx + x;

                if ((next_y < 0 || next_y >= ROWS) || (next_x < 0 || next_x >= COLS)) {
                    continue;
                }
                
                q.push(
                    { std::max(effort, std::abs(heights[next_y][next_x] - heights[y][x])), next_y, next_x}
                );
            }
        } 

        return -1;
    }
};