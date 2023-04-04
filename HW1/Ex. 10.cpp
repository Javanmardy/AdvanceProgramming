#include <iostream>

using namespace std;
int main()
{
    int a, b, c = 0;
    for (int i = 1; i != 0; i++)
    {
        cin >> a;
        if (a == b)
        {
            c = c;
        }
        else
        {
            c = c + 1;
        }

        if (83 > a)
        {
            cout << "too small" << endl;
        }
        else if (83 < a)
        {
            cout << "too large" << endl;
        }
        else
        {
            cout << "It is true" << endl;
            cout << "number of attempts : " << c << endl;
            break;
        }
        b = a;
    }
    return 0;
}