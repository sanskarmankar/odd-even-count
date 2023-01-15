numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count_even = 0
count_odd = 0

NumbersList = list(numbers)

for Num_s in NumbersList:
    if Num_s%2==0:
        count_even += 1
    else:
        count_odd += 1

print("The count of Even Numbers are : " , count_even)
print("The count of Odd Numbers are : " , count_odd)