def reverseArray(inputArray):
    return inputArray[::-1]

if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    print(reverseArray(arr))
