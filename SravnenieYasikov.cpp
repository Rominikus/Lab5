#include <iostream>

int main() {
    int n;
    std::cout << "Введите N: ";
    std::cin >> n;
    long long total = 0;
    for (int i = 1; i <= n; ++i) {
        total += i;
    }
    std::cout << "Сумма: " << total << "\n";
    return 0;
}