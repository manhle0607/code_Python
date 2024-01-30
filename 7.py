def find_three_smallest(arr):
    if len(arr) < 3:
        return "Mảng quá nhỏ, cần ít nhất 3 phần tử."

    smallest = float('inf')
    second_smallest = float('inf')
    third_smallest = float('inf')

    for num in arr:
        if num < smallest:
            third_smallest = second_smallest
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            third_smallest = second_smallest
            second_smallest = num
        elif num < third_smallest:
            third_smallest = num

    return smallest, second_smallest, third_smallest

# Ví dụ
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = find_three_smallest(arr)
print(result)