def filter_num(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if filter_num(num)]



size = int(input())
numbers = []
for i in range(size):
    number = int(input())
    numbers.append((number))

print(filter_prime(numbers))
