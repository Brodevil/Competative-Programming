// Problem Set 2 : Conditional Statements [https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem]

// Author = Abhinav
// Date = 14 July 2022
// Source =  [HackerRank](https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem)

// Solution :

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;

    map<int, string> numbers;
    numbers[0] = "Greater than 9";
    numbers[1] = "one", numbers[2] = "two", numbers[3] = "three", numbers[4] = "four", numbers[5] = "five", numbers[6] = "six", numbers[7] = "seven", numbers[8] = "eight", numbers[9] = "nine";
    
    if (n >= 1 & n <= 9)
    {
        cout<<numbers[n];
    }
    else{
        cout<<numbers[0];
    }
  
    return 0;
}