def arrayMerge(arr1, arr2):
    currIndexArr1 = len(arr1) - 1
    currIndexArr2 = len(arr2) - 1
    for i in arr2:
        arr1.append(0)
    lastIndex = len(arr1) - 1
    while lastIndex > -1:
        if currIndexArr1 > -1 and (currIndexArr2 == -1 or arr1[currIndexArr1] >= arr2[currIndexArr2]):
            arr1[lastIndex] = arr1[currIndexArr1]
            currIndexArr1 -= 1
        else:
            arr1[lastIndex] = arr2[currIndexArr2]
            currIndexArr2 -= 1
        lastIndex -= 1

if __name__ == '__main__':
    userArray1 = [1, 2, 5]
    userArray2 = [3, 4]

    print(f'Unsorted arrays: {userArray1}, {userArray2}')
    arrayMerge(userArray1, userArray2)
    print("Sorted array:\t", userArray1)