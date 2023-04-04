#include <iostream>

using namespace std;

string reverseString(string str);

int main()
{
  string str;
  cin >> str;
  cout << reverseString(str);
}

string reverseString(string str)
{
  char reverse[str.length()]{};
  int i = 0, j = str.length()-1;
  while(i < str.length())
  {
    reverse[i] = str[j];
    i++;
    j--;
  }
  string new_string = "";
  for(int k = 0; k < str.length(); k++)
  {
    new_string += reverse[k];
  }
  return new_string;
}