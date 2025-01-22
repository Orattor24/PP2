def solve(head, legs):
    for chickens in range(head  + 1):
        rabbits = head - chickens
        if 2 * chickens + 4 * rabbits == legs:
            return chickens, rabbits
    return None

a = int(input())
b = int(input())

print(solve(a,b))