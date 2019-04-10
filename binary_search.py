#!/usr/bin/env python3

def binarySearch(arr, value):
    if not arr:
        return -1
    start = 0
    end = len(arr)-1
    mid = int((start+end)/2)
    if arr[mid] == value:
        return mid
    if arr[mid] > value:
        start = start
        end = mid
    else:
        start = mid + 1
        end = end + 1
    index = binarySearch(arr[start:end], value)
    if index < 0:
        return -1
    return start + index



def main():
    arr = range(12)
    print(binarySearch(arr, 3))


if __name__ == '__main__':
    main()
