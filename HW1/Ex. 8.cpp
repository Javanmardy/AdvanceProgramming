#include <iostream>

using namespace std;
int main()
{
    int a, c, d;
    cin >> a;
    for (int i = 1; i <= a; i++)
    {
        c = i;
        for (int j = 2; j <= c; j++)
        {
            d = j;
            if (c % d == 0)
            {
                break;
            }
        }
    }
    if (d == a)
    {
        cout << "prime";
    }
    else
    {
        cout << "not prime";
    }

    return 0;
}