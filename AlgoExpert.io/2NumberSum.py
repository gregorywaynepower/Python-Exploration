array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
    array.sort()
    print(array)
    print(len(array))
    i = 0
    n = 0
    sumArray = []
    for i in array:
        sumArray.append(array[n])
        sumArray.append(array[n+1])
        print("First sumArray")
        print(sumArray)
        i += 1
        sumArraySums = (sumArray[0] + sumArray[1])
        if sumArraySums == targetSum:
            sumArray.sort()
            print(sumArray)
        else:
            sumArray.pop(n+1)
            n += 1
            sumArray.append(n)

        

twoNumberSum(array, targetSum)
