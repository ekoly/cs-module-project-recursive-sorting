# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if start > end:
        return -1

    mid = (start + end)//2
    if arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    else:
        return mid


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):

    if arr[0] < arr[-1]:
        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = (lo + hi)//2
            if target < arr[mid]:
                hi = mid-1
            elif arr[mid] < target:
                lo = mid+1
            else:
                return mid
    else:
        lo, hi = 0, len(arr)-1
        while lo <= hi:
            mid = (lo + hi)//2
            if target > arr[mid]:
                hi = mid-1
            elif arr[mid] > target:
                lo = mid+1
            else:
                return mid

    return -1  # not found
