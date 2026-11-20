struct TrieNode {
    std::unordered_map<char, std::shared_ptr<TrieNode>> children;
    bool is_word = false;
};

class WordDictionary {
public:
    WordDictionary() {
        root = std::make_shared<TrieNode>();
    }
    
    void addWord(string word) {
        auto cur = root; 
        for (char c : word) {
            if (!cur->children.contains(c)) {
                cur->children[c] = std::make_shared<TrieNode>();
            }
            cur = cur->children[c];
        }
        cur->is_word = true;
    }
    
    bool search(string word) {
        return search_recursive(root, word, 0);
    }

private:
    bool search_recursive(std::shared_ptr<TrieNode> node, std::string_view word, std::size_t index) {
        auto cur = node;
        for (int i = index; i < word.length(); i++) {
            char c = word[i];
            if (c == '.') {
                for (auto [charcter, char_node] : cur->children) {
                    if (search_recursive(char_node, word, i + 1)) {
                        return true;
                    }
                }
                return false;
            }
            if (!cur->children.contains(c)) {
                return false;
            }
            cur = cur->children[c];
        }
        return cur->is_word;   
    }

private:
    std::shared_ptr<TrieNode> root;
};
