#include <iostream>

using namespace std;

void test(int j){
  cout <<j;
}
int main(){
  int n = 7;
  float pass = 3;
  float a = pass/n;
  test(n--);
  return 0;
}

