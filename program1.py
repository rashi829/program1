arr = [ ]

for i in range (5):
    num = int(input("enter a number : "))
    arr.append(num)

total = sum (arr)
average = total/5

print("sum = ", total)
print("average =", average)