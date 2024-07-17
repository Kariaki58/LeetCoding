def insertElement(arr, n, x, pos):
    for i in range(n - 1, pos - 1, -1):
        arr[i + 1] = arr[i]
    arr[pos] = x


if __name__=="__main__":
    arr = [2, 4, 1, 8, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    n = 5

    print("Before insertion : ")
    for i in range(0, n):
        print(arr[i],end=' ')

    print("\n")

    x = 10
    pos = 2

    # Function call
    insertElement(arr, n, x, pos);
    n+=1

    print("After insertion : ")
    for i in range(0,n) :
        print(arr[i],end=' ')
