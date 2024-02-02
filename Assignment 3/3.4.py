def minHeapify(numArray, arrLength, indexNum):
    indexMin = indexNum
    indexChildLeft = 2 * indexNum + 1
    indexChildRight = 2 * indexNum + 2

    if indexChildLeft < arrLength and numArray[indexMin] > numArray[indexChildLeft]:
        indexMin = indexChildLeft

    if indexChildRight < arrLength and numArray[indexMin] > numArray[indexChildRight]:
        indexMin = indexChildRight

    if indexMin != indexNum:
        numArray[indexNum], numArray[indexMin] = numArray[indexMin], numArray[indexNum]
        minHeapify(numArray, arrLength, indexMin)

numArray = [8, 12, 9, 7, 22, 3, 26, 14, 11, 15, 22]

print("List:", numArray)
for numIndex in range(len(numArray), -1, -1):
    minHeapify(numArray, len(numArray), numIndex)
print("Heap:", numArray)