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

    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++)
    {
        int length;
        cin >> length;
        arr[i].resize(length);
        for (int j = 0; j < length; j++)
        {
            cin >> arr[i][j];
        }
    }

    for (int k = 0; k < q; k++)
    {
        int i, j;
        cin >> i >> j;
        cout << arr[i][j] << endl;
    }

    return 0;
}