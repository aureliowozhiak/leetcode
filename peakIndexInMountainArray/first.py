# solve with brute force
def peakIndexInMountainArray(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]: # verifico se o atual é maior que o próximo
            return i

print(peakIndexInMountainArray([0,1,3,1,0]))
