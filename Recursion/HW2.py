def lis(arr,i=1,arr_len=None,max_len=None,result=[]):
    
    if arr_len == None and max_len == None:
        arr_len = [1]*len(arr)
        max_len = [None]*len(arr)

    if i == len(arr):
        x = arr_len.index(max(arr_len))

        for y in range(max(arr_len)):
            if y == 0 :
                result +=  [arr[x]]

            else :
                z = max_len[x]
                x = z 
                result+= [arr[x]]
        print(result[::-1])
    else:
        for j in range(i):
            if arr[j] <arr[i]:

                arr_len[i] = arr_len[j]+1
                max_len[i] = j

        lis(arr,i+1,arr_len,max_len,result=[])
                
lis([1,5,2,6,7])


