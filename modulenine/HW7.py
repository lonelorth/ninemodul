def is_prime(func):
    def wrapper(a, b, c):
        n = a + b + c
        list = []
        for i in range(1, 10):
            if n % i == 0:
                list.append(i)
        if len(list) > 2:
            print("Составное")
            return n
        else:
            print("Простое")
            return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(2, 3, 6))