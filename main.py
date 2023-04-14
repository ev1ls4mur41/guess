import random

def guess_number():
    min_number = 0
    max_number = 100
    while True:
        number = random.randint(min_number, max_number)
        print(f"Компьютер предполагает число {number}")
        answer = input("Введите 'больше', 'меньше', 'угадал' или 'выход': ")
        if answer == "выход":
            print("Выход из программы.")
            break
        elif answer == "угадал":
            print("Компьютер угадал число!")
            break
        elif answer == "больше":
            min_number = number + 1
        elif answer == "меньше":
            max_number = number - 1

def guess_number_user():
    number = random.randint(0, 100)
    while True:
        guess = int(input("Введите число от 0 до 100: "))
        if guess == number:
            print("Вы угадали!")
            break
        elif guess < number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

print("Выберите режим игры:")
print("1. Компьютер отгадывает число.")
print("2. Вы отгадываете число.")
mode = input("Введите номер режима: ")
if mode == "1":
    guess_number()
elif mode == "2":
    guess_number_user()
else:
    print("Некорректный ввод.")