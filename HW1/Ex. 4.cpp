#include <iostream>

using namespace std;
int main()
{
    int a, b;
    cout << "number of years employed : ";
    cin >> a;
    cout << "number of children the employee has : ";
    cin >> b;
    cout << "The total amount is " << (20 * a) + (30 * b) + 400 << "$"
         << "."
         << "400$ minimum wage + " << 20 * a << "$"
         << " for " << a << " years experience + " << 30 * b << "$"
         << " for " << b << " kids." << endl;

    return 0;
}
