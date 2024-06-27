from arduan import summa_arduan


def main():
    """
    Это главная функция
    """
    print("Hello World!")


print('Help')  # Это комментарий


def test(a: int, b: int) -> int:
    """
    Это тестовая функция
    """
    return a + b


print(test(1, 2))  # 1+2=3
print(test(5, 8))  # 5+8=11

print("Hello Vitalik!")

a = 1
b = 2

if a > b:
    print("a > b")
else:
    print("a < b")

if __name__ == "__main__":
    main()


def method_name() -> int:
    """

    :return -> int:
    """
    return print(summa_arduan())


method_name()
