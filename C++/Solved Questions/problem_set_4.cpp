// Problem Set 4 : Functions [https://www.hackerrank.com/challenges/c-tutorial-functions/problem]

// Author = Abhinav
// Date = 14 July 2022
// Source =  [HackerRank](https://www.hackerrank.com/challenges/c-tutorial-functions/problem)

// Solution :

#include <iostream>
#include <vector>

using namespace std;

int greatest(int n1, int n2, int n3, int n4)
{
    vector<int> nums;
    nums.push_back(n1);
    nums.push_back(n2);
    nums.push_back(n3);
    nums.push_back(n4);
    
    int great = nums[0];
    for (int i = 1; i < 4; i++)
    {
        if (great < nums[i])
        {
            great = nums[i];
        }
    }
    return great;
}

int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int great = greatest(a, b, c, d);
    cout << great;
    return 0;
}