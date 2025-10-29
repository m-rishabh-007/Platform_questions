using namespace std;
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

struct FileNode {
    map<string, FileNode*> children;
    bool is_directory;
};

class Solution {
public:
    void printTree(FileNode* root) {
        if (!root) return;
        _printRecursive(root, 0);
    }

private:
    void _printRecursive(FileNode* node, int depth) {
        vector<string> keys;
        for (auto it = node->children.begin(); it != node->children.end(); ++it) {
            keys.push_back(it->first);
        }
        sort(keys.begin(), keys.end());

        for (size_t i = 0; i < keys.size(); ++i) {
            string key = keys[i];
            FileNode* child = node->children[key];
            
            for (int d = 0; d < depth; ++d) {
                cout << "  ";
            }

            cout << key;
            if (child->is_directory) {
                cout << "/" << endl;
                _printRecursive(child, depth + 1);
            } else {
                cout << endl;
            }
        }
    }
};

FileNode* parseObject(const string& json, size_t& pos) {
    FileNode* node = new FileNode{{}, true};
    pos++; // skip '{'
    
    while (pos < json.length() && json[pos] != '}') {
        while (pos < json.length() && (json[pos] == ' ' || json[pos] == '\n' || json[pos] == ',')) pos++;
        if (json[pos] == '}') break;
        
        pos++; // skip '"'
        string key;
        while (json[pos] != '"') {
            key += json[pos++];
        }
        pos++; // skip '"'
        
        while (pos < json.length() && (json[pos] == ' ' || json[pos] == ':')) pos++;
        
        if (json[pos] == '{') {
            node->children[key] = parseObject(json, pos);
        } else if (json[pos] == 'n') {
            node->children[key] = new FileNode{{}, false};
            pos += 4; // skip "null"
        }
    }
    pos++; // skip '}'
    return node;
}

int main() {
    string json;
    getline(cin, json);
    
    size_t pos = 0;
    FileNode* root = parseObject(json, pos);
    
    Solution sol;
    sol.printTree(root);
    
    return 0;
}
