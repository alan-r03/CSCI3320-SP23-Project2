def countingSort(inputArray):
    if len(inputArray) > 0 and min(inputArray) > 0:
        outputArray = [0] * len(inputArray)
        countArray = [0] * max(inputArray)
        for num in inputArray:
            countArray[num-1] += 1
        for index in range(1, len(countArray)):
            countArray[index] += countArray[index-1]
        for num in reversed(inputArray):
            outputArray[countArray[num-1]-1] = num
            countArray[num-1] -= 1
        for index in range(len(outputArray)):
            inputArray[index] = outputArray[index]

if __name__ == '__main__':
    userArray = [3, 3, 1, 4, 4]

    print("Unsorted array:", userArray)
    countingSort(userArray)
    print("Sorted array:  ", userArray)