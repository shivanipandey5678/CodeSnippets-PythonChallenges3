//1
N=int(input())
array=list(map(int,input().split()))
salary=int(input())
s=0
for i in range(len(array)):
    s+=array[i]
if(s>salary):
        print("Debt")
elif(s<salary):
        print("Save")
elif(s==salary):
        print("Neutral")
//2
n,m=map(int,input().split())
mat=[]
for i in range(n):
    arr=list(input())
    mat.append(arr)
    c=0
    v=0
for i in range(n):
    for j in range(m):
        if mat[i][j]=="A" or mat[i][j]=="E" or mat[i][j]=="I" or mat[i][j]=="O" or mat[i][j]=="U" :
            v+=1
        elif mat[i][j]!="A" or mat[i][j]!="E" or mat[i][j]!="I" or mat[i][j]!="O" or mat[i][j]!="U" :
            c+=1
print(6*c+9*v)
//3
n=int(input())
s=input()
count=1
res=""
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        count+=1
    else:
        res+=s[i-1]+str(count)
        count=1
res+=s[n-1]+str(count)
print(res)
//4
tc=int(input())
for _ in range(tc):
    n=int(input())
    arr=list(map(int,input().split()))
    subarray_sum=0
    count=0
    target=sum(arr)//3
    for i in range(n):
      subarray_sum+=arr[i]
      if subarray_sum==target:
          subarray_sum=0
          count+=1
    if count>=3:
        print("YES")
    else:
        print("NO")
//5
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr2=list(map(int,input().split()))
    arr.append(arr2)
for i in range(N):
    if(i%2!=0):
        for j in range(M):
            print(arr[i][j],end=" ")
    else:
        for j in range(M-1,-1,-1):
            print(arr[i][j],end=" ")
//6
N,M =list(map(int,input().split()))
mat=[]
for i in range(N):
    row=list(map(int,input().split()))
    mat.append(row)
for i in range(M):
    sumi=0
    for j in range(N):
        if mat[j][i]%2==0:
            sumi+=mat[j][i]
    print(sumi)

