arr=[0,0,0,0,0,0,0]
a=0
count=0
while count<len(arr):
    for i in range(a,len(arr)):
        if arr[i]==0:
            a=i+2
            arr.insert(i,0)
            del arr[len(arr)-1:]
            count+=2
            print(arr)
            break
        else:
            count+=1
print(arr)