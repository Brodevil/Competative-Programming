// Problem Set 3 : For Loop [https://hackerrank.com/challenges/c-tutorial-for-loop/problem]

// Author = Abhinav
// Date = 14 July 2022
// Source =  [HackerRank](https://hackerrank.com/challenges/c-tutorial-for-loop/problem)

// Solution :

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    map<int, string> numbers;
    numbers[0] = "Greater than 9";
    numbers[1] = "one", numbers[2] = "two", numbers[3] = "three", numbers[4] = "four", numbers[5] = "five", numbers[6] = "six", numbers[7] = "seven", numbers[8] = "eight", numbers[9] = "nine";

    int a, b;
    cin >> a >> b;

    for (a; a <= b; a++)
    {
        if (a <= 9)
        {
            cout << numbers[a] << endl;
        }
        else if (a % 2 == 0)
        {
            cout << "even" << endl;
        }
        else
        {
            cout << "odd" << endl;
        }
    }

    return 0;
}