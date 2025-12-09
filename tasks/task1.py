# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())

    numbers = list(map(int, input("Введите числа: ").split()))
    squares = [x ** 2 for x in numbers]
    print(" ".join(map(str, squares)))

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()