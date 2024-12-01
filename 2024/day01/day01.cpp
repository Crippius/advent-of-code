#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <algorithm>
#include <unordered_map>

using namespace std;


void readInput(const string& filename, vector<int>& list1, vector<int>& list2) {
    ifstream file(filename);
    string line;

    while (getline(file, line)) {
        stringstream ss(line);
        int a, b;
        ss >> a >> b;
        list1.push_back(a);
        list2.push_back(b);
    }
}


void part1(vector<int>& list1, vector<int>& list2) {

    sort(list1.begin(), list1.end());
    sort(list2.begin(), list2.end());

    int distance = 0;
    for (int i=0; i<list1.size(); i++) {
        distance += abs(list1[i] - list2[i]);
    }
    cout << "Total distance: " << distance << endl;
}




void part2(vector<int>& list1, vector<int>& list2) {

    unordered_map<int, int> locIdCount;

    int similarity = 0;
    int occurences;
    for (int i=0; i<list1.size(); i++) {
        if (locIdCount.find(list1[i]) == locIdCount.end()) {
            occurences = count(list2.begin(), list2.end(), list1[i]);
            locIdCount[list1[i]] = occurences;
        }
        similarity += list1[i] * locIdCount[list1[i]];
    }
    cout << "Similarity Score : " << similarity << endl;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <input_file>" << endl;
        return 1;
    }

    string inputFile = argv[1];

    vector<int> list1;
    vector<int> list2;
    
    readInput(inputFile, list1, list2);

    part1(list1, list2);
    
    part2(list1, list2);

    return 0;
}