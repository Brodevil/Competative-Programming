// Problem Set 7 : Variable Sized Arrays

// Author = Abhinav
// Date = 16 July 2022
// Source =  [HackerRank](https://www.hackerrank.com/challenges/variable-sized-arrays/problem)

// Solution :

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main()
{
    int n, q;
    cin >> n >> q;

    vector<vector<int>> arr;
    vector<int> temp;
    string input;

    for (int i = 0; i < n; i++)
    {
        cin >> input;
        getline(cin, input);
        istringstream is(input);
        int num;
        while (is >> num)
        {
            temp.push_back(num);
        }
        temp.erase(temp.begin());
        arr[i] = temp;
        temp.clear();      
        
    }

    int i, k;
    for (int i = 0; i < q; i++)
    {
        cin >> i >> k;
        cout<<arr[i][k];
    }

    return 0;
}