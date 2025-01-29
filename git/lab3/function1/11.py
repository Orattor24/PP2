def palindrome(slovo, revslovo):
    vernoe = 0
    for i in range (len(slovo)//2):
        if slovo[i] == revslovo[i]:
            continue
        else:
            print("Не паллиндром")
            break

    print("Палиндром")




slovo = str(input())
revslovo = slovo[::-1]
palindrome(slovo, revslovo)