n = int(input("Введите размер массива: "))
arr =[]
for i in range(n):
    x = int(input(f"Введите элемент {i}: "))
    arr.append(x)
def bubble_sort(arr):
    """Сортировка массива методом пузырька."""
    n = len(arr)
    for i in range(n):
        swapped = False  # оптимизация: если обменов не было — выходим
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
print(f'Отсортированный массив: {bubble_sort(arr)}')
