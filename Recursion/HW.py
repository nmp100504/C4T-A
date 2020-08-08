# def GCD(a,b):
#     if a == 0 :
#         return b
#     if b == 0:
#         return a
#     if a != 0 or b !=0:
#         if a > b :
#             return GCD(b,a%b)
#         if a < b:
#             return GCD(a,b%a)


# print(GCD(270,192))


# def lt(x,n):
#     if n == 0:
#         return 1
#     if  n > 0 :
#         return lt(x,n-1)*x
#     if n < 0 :
#         return lt(x,-n-1)*x

# print(lt(2,-5))


# def recurCount(arr,x):
#     if arr == []: 
#         return 0
#     if arr[0] == x:
#         return recurCount(arr[1:],x) +1
#     return recurCount(arr[1:],x)

# print(recurCount([2,5,8,9,12,2,2,2],2)) 


# def GCD(a,b):
#     if a % b ==0  :
#         return b
#     return GCD(b,a%b)

# print(GCD(192,270))




# def binary_search(arr, low, high, x): 
#     if high >= low: 
#         mid = (high + low) // 2
#         if arr[mid] == x: 
#             return mid 
#         elif arr[mid] > x: 
#             return binary_search(arr, low, mid - 1, x) 
#         else: 
#             return binary_search(arr, mid + 1, high, x) 
#     else: 
#         return -1
  

# arr = [1, 2, 3, 5, 100] 
  
# result = binary_search(arr, 0, len(arr)-1, 5) 
  
# if result != -1: 
#     print("Element is present at index", str(result)) 
# else: 
#     print("Element is not present in array") 


# def sum(arr):

#     if len(arr)==1:
#         return arr[0]
#     if len(arr)==0:
#         return 0
#     mid = len(arr) // 2 
#     return sum(arr[:mid]) +sum(arr[mid:])


# def pesa(arr,i,left_arr=None,right_arr=[]):
#     if left_arr == None:
#         left_arr = [arr[0]]
#     if i == len(arr):
#         if sum(right_arr) == sum(left_arr):
#             print(right_arr,left_arr)
#     if i < len(arr) :

#         pesa(arr,i+1,left_arr+[arr[i]],right_arr)
#         pesa(arr,i+1,left_arr,right_arr+[arr[i]])
#         # pesa(arr,i+1,left_arr,right_arr)
        
# pesa([1,2,3,5,6,5],1)


arr = [1,5,3,2,9,7]
def tla(arr,n=0,arr_2=[],i=0):
    if i == len(arr):
        print(arr_2)
    elif arr[i]>arr[i-1] : 
        tla(arr,arr[i],arr_2,i+1)
        tla(arr,arr[i],arr_2+[arr[i]],i+1)

tla(arr)
