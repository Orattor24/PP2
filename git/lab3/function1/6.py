def reverse(sentence):
    return ' '.join(sentence.split()[::-1])
s = str(input())
print(reverse(s))