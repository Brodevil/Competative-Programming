// Problem Set 5 : Pointers [https://www.hackerrank.com/challenges/c-tutorial-pointer/problem]

// Author = Abhinav
// Date = 15 July 2022
// Source =  [HackerRank](https://www.hackerrank.com/challenges/c-tutorial-pointer/problem)

// Solution :

#include <iostream>

using namespace std;

void update(int *a, int *b)
{
    int _a = *a;
    int _b = *b;

    if (_a > _b)
    {
        *b = _a - _b;
    }
    else if (_b > _a)
    {
        *b = _b - _a;
    }
    else
    {
        *b = 0;
    }

    *a = _a + _b;
}

int main()
{
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}