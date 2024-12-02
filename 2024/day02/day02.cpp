#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <algorithm>
#include <unordered_map>

using namespace std;


vector<vector<int>> readInput(const string& filename) {
    vector<vector<int>> data;
    ifstream file(filename);
    string line;

    if (!file.is_open()) {
        cerr << "Error: Could not open file " << filename << endl;
        exit(1);
    }

    while (getline(file, line)) {
        stringstream ss(line);
        vector<int> row;
        int num;
        while (ss >> num) {
            row.push_back(num);
        }
        data.push_back(row);
    }

    return data;
}

bool isSafeIncreasing(vector<int>& row) {
    int dist;
    for (int i=0; i<row.size()-1; i++) {
        dist = row[i+1] - row[i];
        if (dist <= 0 or dist > 3)
            return false;
    }
    return true;
}

bool isSafeDecreasing(vector<int>& row) {
    int dist;
    for (int i=0; i<row.size()-1; i++) {
        dist = row[i] - row[i+1];
        if (dist <= 0 or dist > 3)
            return false;
    }
    return true;
}

bool isSafe(vector<int>& row) {
    if (row.size() <= 1)
        return true;
    if (row[0] < row[1])
        return isSafeIncreasing(row);
    if (row[0] > row[1])
        return isSafeDecreasing(row);
    return false;
    
    
}


bool isSafeWithRemoval(const vector<int>& list) {
    for (int i = 0; i < list.size(); ++i) {
        vector<int> new_list;
        for (int j = 0; j < list.size(); ++j) {
            if (j != i) new_list.push_back(list[j]);
        }
        if (isSafe(new_list)) return true;
    }
    return false;
}


void part1(vector<vector<int>>& list) {
    int safe = 0;
    for (vector<int> row : list)
        safe += isSafe(row);
    
    cout << "Safe reports: " << safe << endl;
}




void part2(vector<vector<int>>& list) {
    int safe = 0;
    for (vector<int> row : list)
        safe += isSafeWithRemoval(row);
    
    cout << "Safe reports: " << safe << endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }

    string inputFile = argv[1];

    vector<vector<int>> list;
    
    list = readInput(inputFile);

    part1(list);

    part2(list);

    return 0;
}