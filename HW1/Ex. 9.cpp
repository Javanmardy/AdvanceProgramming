#include <iostream>

using namespace std;
int main()
{
    int a, b, c, d;
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
        if (c == d)
        {
            cout << c;
        }
    }
    return 0;
}