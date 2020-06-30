# arr =[2 ,4, 5, 1, 2,5, 7 ]
# def sum(arr):
#     if len(arr)==1:
#         return arr[0]
#     return sum(arr[:mid]) +sum(arr[mid:])

# print(sum(arr))
string ="Hello"
def reverse(string):
    if len(string) ==1:
        return string[0]
    return reverse(string[1:])+ string[0]
print(reverse(string))

    
