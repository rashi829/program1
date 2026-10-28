def find_largest_and_smallest():
    numbers = []
    print("please enter 10 number")

 # take 10 inputs from the user
    for i in range(10):
        num = float(input(f"Enter number{i+1}:"))
        numbers.append(num)
 # assume the first element is both largest and smallest initally
    largest = numbers[0]
    smallest = numbers[0]
# traverse through the list to find largest and smallest for num in number[1:]:
    if num > largest:
     largest = num
    if num < smallest:
     smallest = num
# display results
    print(f"\n The numbers enterted are: {numbers}")
    print(f" the largest number is: {largest}")
    print(f"the smallest is:{smallest}")


find_largest_and_smallest()