#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

// ===== PLATFORM INJECTION POINT =====
// The contestant's Solution class will be injected here by the platform
// DO NOT UNCOMMENT OR MODIFY THIS SECTION
// ===== END INJECTION POINT =====

// Simple JSON parser for this specific problem
FileNode* parseJSON(const string& json, size_t& pos);

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
