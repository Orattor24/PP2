def spy_game(nums):
    problema = 0
    nums2 = []
    for i in range(len(nums)):
        if nums[i] == 0:
            nums2.append(nums[i])
        if nums[i] == 7:
            nums2.append(nums[i])
    if nums2[0] ==0 and nums2[1] == 0 and nums2[2] == 7:
        return True
    else:
        return False

spis = []
num=int(input())
for i in range(num):
    chislo = int(input())
    spis.append(chislo)
print(spy_game(spis))