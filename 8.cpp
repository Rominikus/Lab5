// #include <iostream>
// #include <iomanip>
// #include <string>

// Задание 3
// int main() {
//     // Вывод заголовка с выравниванием по правому краю
//     std::cout << std::setw(8) << "x" << std::setw(17) << "x**2 - 2*x + 1" << "\n";
    
//     // Вывод разделительной линии (30 дефисов)
//     std::cout << std::string(30, '-') << "\n";

//     // Цикл от -5 до 5 включительно
//     for (int i = -5; i <= 5; ++i) {
//         int y = i * i - 2 * i + 1;
//         // Форматируем вывод: 8 символов для x, 10 символов для y
//         std::cout << std::setw(8) << i << std::setw(10) << y << "\n";
//     }

//     return 0;
// }

// Задание 6
// #include <iostream>
// #include <string>

// int main() {
//     std::cout << "Выберите 1 или 2.\n";
//     std::cout << "1) Перевести из двоичной в десятичную\n";
//     std::cout << "2) Перевести из десятичной в двоичную\n";
//     std::cout << "(1/2?) ";
    
//     int ans;
//     if (!(std::cin >> ans)) {
//         std::cout << "Некорректный ввод, перезапустите программу\n";
//         return 1;
//     }

//     if (ans == 1) {
//         long long n;
//         std::cout << "Введите целое число в двоичной системе счисления: ";
//         std::cin >> n;
        
//         long long res = 0;
//         long long temp = n;
//         long long multiplier = 1; // Аналог 2 ** m
        
//         while (temp > 0) {
//             int digit = temp % 10;
//             res += digit * multiplier;
//             multiplier *= 2;      // Увеличиваем степень двойки
//             temp /= 10;
//         }
        
//         std::cout << n << " в десятичной будет: " << res << "\n";
        
//     } else if (ans == 2) {
//         long long n;
//         std::cout << "Введите целое число: ";
//         std::cin >> n;
        
//         // Обработка крайнего случая для 0
//         if (n == 0) {
//             std::cout << n << " в двоичной будет: 0\n";
//         } else {
//             std::string res = "";
//             long long temp = n;
            
//             while (temp > 0) {
//                 // Преобразуем остаток от деления в строку и добавляем в начало
//                 res = std::to_string(temp % 2) + res;
//                 temp /= 2;
//             }
            
//             std::cout << n << " в двоичной будет: " << res << "\n";
//         }
//     } else {
//         std::cout << "Некорректный ввод, перезапустите программу\n";
//     }

//     return 0;
// }