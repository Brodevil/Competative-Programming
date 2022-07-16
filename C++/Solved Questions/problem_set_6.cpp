// Problem Set 6 : Arrays Introductor [https://hackerrank.com/challenges/arrays-introduction/problem]

// Author = Abhinav
// Date = 15 July 2022
// Source =  [HackerRank](https://hackerrank.com/challenges/arrays-introduction/problem)

// Solution :

#include <iostream>

using namespace std;

int main()
{
    int n, i = 0;
    cin >> n;
    int *A = new int[n];
    
    while (cin >> A[i++]);
    
    while (cout << A[--n] << ' ' && n);
    delete[] A;
    
    return 0;
}