#include <iostream>

using namespace std;
int main()
{
    int a, b = 0, c = 1, d;
    cin >> a;
    for (int i = 0; i != a - 1; i++)
    {
        d = b + c;
        b = c;
        c = d;
    }
    cout << d << endl;
    return 0;
}