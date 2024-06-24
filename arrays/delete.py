def removeFromArray(arr, n, pos):
    for i in range(pos - 1, n - 1):
        arr[i] = arr[i + 1]
    del arr[len(arr) - 1]
    return arr

if __name__=="__main__":
    arr = [10, 50, 30, 40, 20]

    pos = 3
    print("array before deletion")

    print(arr)

    arr = removeFromArray(arr, 5, pos)
    print("array after deletion")
    print(arr)

