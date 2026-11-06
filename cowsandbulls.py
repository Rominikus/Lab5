import random

def bulls_and_cows():
    # Загадываем число из 4 уникальных цифр
    secret = random.sample(range(10), 4)
    print("Я загадал 4-значное число. Угадай!")
    
    while True:
        guess = input("Твой вариант (4 цифры): ")
        if len(guess) != 4 or not guess.isdigit():
            print("Нужно ввести ровно 4 цифры!")
            continue
            
        guess = [int(x) for x in guess]
        
        # Считаем быков (угадал цифру и её позицию)
        bulls = sum(1 for s, g in zip(secret, guess) if s == g)
        # Считаем коров (угадал цифру, но не позицию)
        cows = sum(1 for g in guess if g in secret) - bulls
        
        print(f"🐂 Быков: {bulls} | 🐄 Коров: {cows}")
        
        if bulls == 4:
            print("🎉 Ты угадал!")
            break

bulls_and_cows()