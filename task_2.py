k = int(input('Введите кол-во кустов: '))
arr = list()
for i in range(k):
    x = int(input('Введите кол-во ягод на кусте: '))
    arr.append(x)
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))
