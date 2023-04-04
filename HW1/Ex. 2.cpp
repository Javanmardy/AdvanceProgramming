#include <iostream>

using namespace std;
int main()
{
    int a, b;
    b = 1;
    cin >> a;
    for (int i = 0; a != 0; i++)
    {
        for (int i = 0; a - i != 0; i++)
        {
            cout << "*";
        }
        for (int j = 1; j != (2 * b) - 1; j++)
        {
            cout << " ";
        }
        for (int i = 0; a - i != 0; i++)
        {
            cout << "*";
        }
        a = a - 1;
        b = b + 1;
        cout << endl;
    }

    return 0;
}
