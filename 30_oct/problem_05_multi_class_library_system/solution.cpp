using namespace std;
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iostream>

class Solution {
private:
    struct Book {
        string author;
        bool checked_out;
        int checked_out_by;
    };
    
    vector<string> parseCommand(const string& cmd) {
        vector<string> parts;
        bool in_quote = false;
        string current;
        
        for (char c : cmd) {
            if (c == '"') {
                in_quote = !in_quote;
            } else if (c == ' ' && !in_quote) {
                if (!current.empty()) {
                    parts.push_back(current);
                    current.clear();
                }
            } else {
                current += c;
            }
        }
        
        if (!current.empty()) {
            parts.push_back(current);
        }
        
        return parts;
    }

public:
    vector<string> processCommands(vector<string>& commands) {
        map<string, Book> books;
        map<int, string> members;
        vector<string> results;
        
        for (const string& cmd : commands) {
            vector<string> parts = parseCommand(cmd);
            
            if (parts[0] == "ADD" && parts[1] == "BOOK") {
                string title = parts[2];
                string author = parts[3];
                
                if (books.find(title) == books.end()) {
                    books[title] = {author, false, -1};
                    results.push_back("Book \"" + title + "\" added.");
                }
                
            } else if (parts[0] == "ADD" && parts[1] == "MEMBER") {
                string name = parts[2];
                int member_id = stoi(parts[3]);
                
                if (members.find(member_id) == members.end()) {
                    members[member_id] = name;
                    results.push_back("Member \"" + name + "\" registered.");
                }
                
            } else if (parts[0] == "CHECKOUT") {
                int member_id = stoi(parts[1]);
                string title = parts[2];
                
                if (members.find(member_id) == members.end()) {
                    results.push_back("Error: Member not found.");
                } else if (books.find(title) == books.end()) {
                    results.push_back("Error: Book not found.");
                } else if (books[title].checked_out) {
                    results.push_back("Error: Book not available.");
                } else {
                    books[title].checked_out = true;
                    books[title].checked_out_by = member_id;
                    results.push_back("Checkout successful.");
                }
                
            } else if (parts[0] == "RETURN") {
                string title = parts[1];
                
                if (books.find(title) == books.end() || !books[title].checked_out) {
                    results.push_back("Error: Book not in records or was not checked out.");
                } else {
                    books[title].checked_out = false;
                    books[title].checked_out_by = -1;
                    results.push_back("Return successful.");
                }
            }
        }
        
        return results;
    }
};

int main() {
    vector<string> commands;
    string line;
    
    while (getline(cin, line) && line != "EXIT") {
        commands.push_back(line);
    }
    
    Solution sol;
    vector<string> results = sol.processCommands(commands);
    
    for (const string& result : results) {
        cout << result << endl;
    }
    
    return 0;
}
