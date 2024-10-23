# quicksort is a recursive algorithm - follows divide and conquer strategy by selecting pivot
# TC - best and average O(n logn)
# worst - O(n^2)
# as quicksort is recursive it maintains a recursion stack which requires additional memory
# space complecit - worst: O(n), avg: O(logn)

# The iterative approach is more efficient than recursive.

# Recursion in Quick Sort is generally efficient for most cases, but it's important to understand 
# its limitations (like the worst case). If your concern is worst-case performance, 
# you might want to consider using Merge Sort or hybrid sorting algorithms like Timsort. 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []

        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)

        return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    arr = [9,7,5,11,12,2,14,3,10,6]
    print("Original array : ", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array : ", sorted_arr)

