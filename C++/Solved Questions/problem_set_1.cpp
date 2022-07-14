// Problem Set 1 : Basic Data Types [https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem]

// Author = Abhinav
// Date = 14 July 2022
// Source =  [HackerRank](https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem)

// Solution :

#include <iostream>

using namespace std;

int main()
{
    int a;
    long int b;
    char c;
    float d;
    double e;

    scanf("%d %ld %c %f %lf", &a, &b, &c, &d, &e);
    printf("%d\n", a);
    printf("%ld\n", b);
    printf("%c\n", c);
    printf("%f\n", d);
    printf("%lf", e);

    return 0;
}
