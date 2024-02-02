def maxHeapify(numArray, arrLength, indexNum):
    indexMin = indexNum
    indexChildLeft = 2 * indexNum + 1
    indexChildRight = 2 * indexNum + 2

    if indexChildLeft < arrLength and numArray[indexMin] < numArray[indexChildLeft]:
        indexMin = indexChildLeft

    if indexChildRight < arrLength and numArray[indexMin] < numArray[indexChildRight]:
        indexMin = indexChildRight

    if indexMin != indexNum:
        numArray[indexNum], numArray[indexMin] = numArray[indexMin], numArray[indexNum]
        maxHeapify(numArray, arrLength, indexMin)

def largestNumbers(numArray, amtNums):
    arrLargest = []

    for i in range(amtNums):
        for numIndex in range(len(numArray), -1, -1):
            maxHeapify(numArray, len(numArray), numIndex)

        numArray[0], numArray[-1] = numArray[-1], numArray[0]
        arrLargest.append(numArray.pop())

    return arrLargest

numArray = [3, 10, 1000, -99, 4, 100]
numTargets = 3

print(largestNumbers(numArray, numTargets))