def bubbleSort(arr):
    n = len(arr)
    steps = 1
    
    for i in range(n - 1):
        swapped = False # Check list đã được sort xong chưa. Nếu True -> Chỉ do if cần sắp xếp -> Cần check tiếp. Nếu False -> sort xong
        for j in range(n - i - 1):
            print("step", steps, ":")
            steps += 1
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return arr


arr = [4, 6, 7, 9]

print(bubbleSort(arr))