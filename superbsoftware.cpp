#include <iostream>
#include <random>

int main() {
    srand(time(0));
    std::cout << rand() % 10000 << std::endl;
    return 0;
}
