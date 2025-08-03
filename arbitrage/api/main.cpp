#include <iostream>
#include <vector>
#include <map>
#include <pybind11/pybind11.h>
#include <string>
#include <optional>

using namespace std;
struct MinMax {
    optional<double> min;
    optional<double> max;
};

struct Precision {
    optional<int> price;  // or double if fractional precision is needed
    optional<int> amount;
    optional<int> cost;
};

struct Limits {
    MinMax amount;
    MinMax price;
    MinMax cost;
    MinMax leverage;
    // Add more if needed, e.g., for other limit types like 'market' or exchange-specific ones
};

struct MarginModes {
    bool cross = false;
    bool isolated = false;
};

struct Market {
    string id;
    string symbol;
    string base;
    string quote;
    optional<string> baseId;   // Optional as not all exchanges provide it
    optional<string> quoteId;  // Optional as not all exchanges provide it
    optional<bool> active;          // Boolean, optional if status unknown
    string type;                    // e.g., "spot", "future", etc.
    bool spot = false;
    bool margin = false;
    bool future = false;
    bool swap = false;
    bool option = false;
    bool contract = false;
    optional<string> settle;   // Unified currency code for settlement
    optional<string> settleId; // Exchange-specific settlement ID
    optional<double> contractSize;  // Size of one contract
    optional<bool> linear;          // True for linear contracts
    optional<bool> inverse;         // True for inverse contracts
    optional<long long> expiry;     // Unix timestamp in ms, for futures
    optional<string> expiryDatetime; // ISO8601 string
    optional<double> strike;        // For options
    optional<string> optionType; // "call" or "put"
    optional<double> taker;         // Taker fee rate
    optional<double> maker;         // Maker fee rate
    bool percentage = true;              // Whether fees are percentage-based
    bool tierBased = false;              // Whether fees are tier-based
    string feeSide;                 // "get", "give", etc.
    Precision precision;
    Limits limits;
    MarginModes marginModes;
    map<string, string> info; // Arbitrary key-value pairs for exchange-specific data
};

long long f(int n){
    long long out = 1;
    for (int i = 2; i <= n; i++) {
        out *= i;
    }
    return out;
}

long long a(int n){
    return n;
}

int test(Market m) {
    return 0;
};

PYBIND11_MODULE(api, m) {
    m.doc() = "ex binding";
    m.def("factorial", &f, "factorial fn");
    m.def("a", &a, "test");
}
