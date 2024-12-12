import math


def check_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    print(check_prime(351))
