struct TrieNode {
    TrieNode() = default;

    std::unordered_map<char, std::shared_ptr<TrieNode>> children;
    bool is_word;
};

class PrefixTree {
public:
    PrefixTree() {
        root = std::make_shared<TrieNode>();
    }
    
    void insert(string word) {
        std::shared_ptr<TrieNode> cur = this->root;
        for (char c : word) {
            if (!cur->children.contains(c)) {
                cur->children[c] = std::make_shared<TrieNode>();
            }
            cur = cur->children[c];
        }
        cur->is_word = true;
    }
    
    bool search(string word) {
        std::shared_ptr<TrieNode> cur = this->root;
        for (char c : word) {
            if (!cur->children.contains(c)) {
                return false;
            }
            cur = cur->children[c];
        }
        return cur->is_word;     
    }
    
    bool startsWith(string prefix) {
        std::shared_ptr<TrieNode> cur = this->root;
        for (char c : prefix) {
            if (!cur->children.contains(c)) {
                return false;
            }
            cur = cur->children[c];
        }
        return true;
    }

private:
    std::shared_ptr<TrieNode> root;
};
