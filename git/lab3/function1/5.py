def string_permutations(s):
    def permute(prefix, remaining, results):
        if len(remaining) == 0:
            results.append(prefix)
        else:
            for i in range(len(remaining)):
                new_prefix = prefix + remaining[i]
                new_remaining = remaining[:i] + remaining[i + 1:]
                permute(new_prefix, new_remaining, results)

    results = []
    permute("", s, results)
    return results

s = str(input())

print(string_permutations(s))
