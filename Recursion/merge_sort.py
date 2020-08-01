# arr_1 = [3,4,5]
# arr_2 =[1,2,6,7]

def merge(left,right):
    arr_merge = []
    while len(left) and len(right) !=0:
        if left[0] < right[0]:
            arr_merge.append(left.pop(0))
        else:
            arr_merge.append(right.pop(0))
    arr_merge +=left+right
    return arr_merge

# print(merge(arr_1,arr_2))

arr = [2,5,3,1,4,7,6]

def sort(arr):
    if len(arr) <= 1 :
        return arr
    mid = len(arr) // 2 
    return merge(sort(arr[0:mid]),sort(arr[mid:]))


print(sort(arr))

    