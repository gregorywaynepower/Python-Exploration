array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
    array.sort()
    print(array)
    print(len(array))
    i = 0
    n = 0
    sumArray = []
    while len(sumArray) < 2:
        sumArray.append(array[n])
        sumArray.append(array[n+1])
        print("First sumArray")
        print(sumArray)
        i += 1
        sumArraySums = (sumArray[0] + sumArray[1])
        k = 0
        if sumArraySums != targetSum:
            sumArray.pop()
            k += 1
            sumArray.append(array[i])
        elif sumArraySums == targetSum:
            return sumArray
        else:
            sumArray = []
            return sumArray
        

        

twoNumberSum(array, targetSum)
