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
#     if n != 1:
#         return lt(x,n-1)*x
# print(lt(2,5))

arr = [2, 5, 8, 9, 2]
counted = 0
def count(arr,x,counted):
    if arr[0] == x :
        return counted+1
    return count(arr[1:],x,counted) 
print(count(arr,2,counted))