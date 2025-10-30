def hourGlassSum(subArray, i , j): return subArray[i][j] + subArray[i][j+1] + subArray[i][j+2] + subArray[i+1][j+1] + subArray[i+2][j] + subArray[i+2][j+1] + subArray[i+2][j+2]

def hourGlassMaxSum(mainArray):
    hourGlassMaxSum = float('-inf')
    for i in range(len(mainArray)-2):
        for j in range(len(mainArray)-2):
            calculatedSum = hourGlassSum(mainArray, i, j)
            hourGlassMaxSum = max(hourGlassMaxSum, calculatedSum)
    return hourGlassMaxSum

if __name__ == "__main__":
    arr = []
    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourGlassMaxSum(arr))
