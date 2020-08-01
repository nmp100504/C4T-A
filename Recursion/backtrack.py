# coin_arr=[]
# def coin_choose(n,arr,choose,i=0):
#     if n == 0 :
#         print(choose)
#     elif n>0 :
#         for j in range(i,len(arr)):
#             coin_choose(n-arr[j],arr,choose+[arr[j]],j)
        

# coin_choose(10,[1,2,5],coin_arr)


# def coin_choose(n,choose=""):
#     if n == 0 :
#         print(choose)
#     elif n>0 :
#         coin_choose(n-1,choose+"0")
#         coin_choose(n-1,choose+"1")
        

# coin_choose(3)

def sum(arr):
    if len(arr)==1:
        return arr[0]
    if len(arr)==0:
        return 0
    mid = len(arr) // 2 
    return sum(arr[:mid]) +sum(arr[mid:])
def subset(arr,i=0,choose=[],chosen_dict={}):
    if i ==len(arr):
        chosen_dict[sum(choose)]=choose
        print(chosen_dict)
    if i < len(arr):
        subset(arr,i+1,choose+[arr[i]])
        subset(arr,i+1,choose)
subset([1,2,3,5])
# for i in range(len(dict)):
        
