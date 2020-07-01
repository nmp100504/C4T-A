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
#     if n == 1:
#         return x
#     return lt(x,n-1)*x

# print(lt(2,5))


# def recurCount(arr,x):
#     if arr == []: 
#         return 0
#     if arr[0] == x:
#         return 1 + recurCount(arr[1:],x)
#     else:
#         return 0 + recurCount(arr[1:],x)

# print(recurCount([2,5,8,9,12,2,2,2],2)) 