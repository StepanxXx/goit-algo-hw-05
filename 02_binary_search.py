def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0

    while low <= high:
        count += 1

        mid = (high + low) // 2


        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return (count, arr[mid])

    # якщо елемент не знайдений
    if arr[mid] >= x:
        return (count, arr[mid])
    else:
        return (count, None)

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 6
    result = binary_search(arr, x)
    if result[1] == x:
        print(f"Element is present: {result}")
    else:
        print(f"Element is not present in array: {result}")
