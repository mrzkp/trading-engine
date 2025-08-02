#include <iostream>
#include <pybind11/pybind11.h>

using namespace std;


long long factorial(int n){
    long long out = 1;
    for (int i = 2; i <= n; i++) {
        out *= i;
    }
    return out;
}

int main(){
    return 0;
}

PYBIND11_MODULE(api_module, m) {

}
