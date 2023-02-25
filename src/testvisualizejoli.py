def mergeSort (arr,i,j):
    if i < j:
        mid = (i+j)//2
        mergeSort(arr,i,mid)
        mergeSort(arr,mid+1,j)
        merge(arr,i,mid,j)
def merge(arr,i,mid,j):
    n1 = i
    n2 = mid+1
    temp = []
    while n1 <= mid and n2 <= j:
        if arr[n1] < arr[n2]:
            temp.append(arr[n1])
            n1 += 1
        else:
            temp.append(arr[n2])
            n2 += 1
    while n1 <= mid:
        temp.append(arr[n1])
        n1 += 1
    while n2 <= j:
        temp.append(arr[n2])
        n2 += 1
    for k in range(len(temp)):
        arr[i+k] = temp[k]

arr = [2,4,1,6,8,5,3,7]
mergeSort(arr,0,len(arr)-1)

print(arr)

def selectionSort(arr,i,j):
    if i < j:
        k = i
        selectionSort(arr,k+1,j)
        combine(arr,i,k,j)

def combine(arr,i,k,j):
    p = k+1
    while arr[p-1] > arr[p] and p < j:
        arr[p-1],arr[p] = arr[p],arr[p-1]
        p += 1
    if arr[p-1] > arr[p]:
        arr[p-1],arr[p] = arr[p],arr[p-1]

arr = [2,4,1,6,8,5,3,7]
selectionSort(arr,0,len(arr)-1)
print(arr)