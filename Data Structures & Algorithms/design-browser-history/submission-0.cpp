class BrowserHistory {
public:
    BrowserHistory(string homepage)
        : homepage_(homepage), current_page_(homepage) {
        
    }
    
    void visit(string url) {
        undo_.push(current_page_);
        current_page_ = url;
        redo_ = {};
    }
    
    string back(int steps) {
        int max_steps = std::min(static_cast<int>(undo_.size()), steps);

        for(int i = 0; i < max_steps; i++) {
            redo_.push(current_page_);
            current_page_ = undo_.top();
            undo_.pop();
        }

        if (steps > max_steps) {
            return homepage_;
        }
        return current_page_;
    }
    
    string forward(int steps) {
        int max_steps = std::min(static_cast<int>(redo_.size()), steps);

        for(int i = 0; i < max_steps; i++) {
            undo_.push(current_page_);
            current_page_ = redo_.top();
            redo_.pop();
        }

        return current_page_;        
    }

private:
    std::string homepage_;
    std::string current_page_;
    std::stack<std::string> undo_;
    std::stack<std::string> redo_;
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */