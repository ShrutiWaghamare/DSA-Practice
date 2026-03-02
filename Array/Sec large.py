def seclargest(arr):
    lar = -1
    seclar = -1
    for i in range(len(arr)):
        if arr[i] > lar:
            seclar = lar
            lar = arr[i]
        elif arr[i] < lar and arr[i] > seclar:
            seclar = arr[i]
    return seclar
    
arr = [12, 35, 1, 10, 34, 1]
print(seclargest(arr))