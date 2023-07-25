import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def main():
    try:
        size = int(input("Enter the size of the list: "))
        lower_bound = int(input("Enter the lower bound of random numbers: "))
        upper_bound = int(input("Enter the upper bound of random numbers: "))

        if size <= 0 or lower_bound >= upper_bound:
            print("Invalid input. Please provide valid parameters.")
            return

        random_list = generate_random_list(size, lower_bound, upper_bound)
        print("Generated Random List:", random_list)

        sorted_list = bubble_sort(random_list)
        print("Sorted List:", sorted_list)

    except ValueError:
        print("Invalid input. Please provide valid integers.")

if __name__ == "__main__":
    main()
