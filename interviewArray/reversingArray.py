def reverse_array_extra_array(arr):
    # pass in an array to reverse with another array
    reversed_arr = arr[::-1]
    
    print("Reversed Array:", end="\n")
    for i in reversed_arr:
        print(i, end = ' ')
    print('')

def reverseListTwoPointer(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
        
def reverseListRecursion(A, start, end):
    if start >= end:
        A[start], A[end] = A[end], A[start]
        reverseListRecursion(A, start+1, end-1)