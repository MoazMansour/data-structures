#!/usr/bin/env python3

def binarySearch(arr, value):
    start = 0
    end = len(arr)-1
    while start != end:
        mid = int((start+end)/2)
        if arr[mid] == value:
            return mid
        if arr[mid] > value:
            start = start
            end = mid - 1
            continue
        else:
            start = mid + 1
            end = end
    if arr[start] == value:
        return start
    return -1


def main():
    arr = range(12)
    print(binarySearch(arr, 11))


if __name__ == '__main__':
    main()
