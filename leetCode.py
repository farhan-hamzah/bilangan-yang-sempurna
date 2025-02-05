# Perfect Number
nums = int(input())
i = 0
hasil = 0
for i in range (1, nums):
    if nums%i == 0:
        hasil = hasil + i
if hasil == nums:
    t = True
    print(t)
else:
    t = False
    print(t)

