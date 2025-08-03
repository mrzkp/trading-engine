#include <iostream>
#include <pybind11/pybind11.h>

long long f(int n){
    long long out = 1;
    for (int i = 2; i <= n; i++) {
        out *= i;
    }
    return out;
}

PYBIND11_MODULE(api, m) {
    m.doc() = "ex binding";
    m.def("factorial", &f, "factorial fn");
}
