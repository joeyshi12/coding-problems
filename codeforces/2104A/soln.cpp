#include <iostream>
#include <ostream>
#include <vector>

int main() {
    int n, a, b, c, k1, k2;
    std::cin >> n;
    std::vector<bool> answers(n, false);
    for (int i = 0; i < n; i++) {
        std::cin >> a;
        std::cin >> b;
        std::cin >> c;
        k1 = -a * 2 + b + c;
        k2 = a - b * 2 + c;
        if (k1 >= 0 && k1 % 3 == 0 && k2 >= 0 && k2 % 3 == 0) {
            answers[i] = true;
        }
    }
    for (bool ans : answers) {
        if (ans) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }
}
