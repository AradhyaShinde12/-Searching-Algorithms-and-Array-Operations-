def linear_search(arr):
    key = int(input("Enter element to search: "))

    for i in range(len(arr)):
        if arr[i] == key:
            print("Element found at index:", i)
            return

    print("Element not found.")

def binary_search(arr):
    # Binary search requires a sorted array
    sorted_arr = sorted(arr)
    print("Sorted array:", sorted_arr)

    key = int(input("Enter element to search: "))

    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_arr[mid] == key:
            print("Element found at index:", mid,
                  "in the sorted array")
            return
        elif sorted_arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("Element not found.")

def reverse_array(arr):
    reversed_arr = arr[::-1]
    print("Reversed array:", reversed_arr)

def find_max_min(arr):
    print("Maximum element:", max(arr))
    print("Minimum element:", min(arr))

def sum_array(arr):
    total = sum(arr)
    print("Sum of array elements:", total)

def main():
    n = int(input("Enter the number of array elements: "))

    while n <= 0:
        print("Please enter a positive number.")
        n = int(input("Enter the number of array elements: "))

    arr = []

    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    while True:
        print("\n====== MENU ======")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Reverse Array")
        print("4. Find Maximum and Minimum")
        print("5. Sum of Array Elements")
        print("6. Display Array")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            linear_search(arr)

        elif choice == '2':
            binary_search(arr)

        elif choice == '3':
            reverse_array(arr)

        elif choice == '4':
            find_max_min(arr)

        elif choice == '5':
            sum_array(arr)

        elif choice == '6':
            print("Array:", arr)

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1 to 7.")

if __name__ == "__main__":
    main()



