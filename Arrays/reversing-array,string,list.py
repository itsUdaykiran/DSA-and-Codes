#Iterative way
def reverse(A,start,end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1
        
A=[1,2,3,4,5,6]
print(A)
reverse(A,0,5)
print("reversed array/string/list: ")
print(A)

#Recursive way
def reverse(A,start,end):
    if start>=end:
        return
    A[start], A[end] = A[end], A[start]
    reverse(A,start+1,end-1)
 
A=[1,2,3,4,5,6]
print(A)
reverse(A,0,5)
print("reversed array/string/list: ")
print(A)

#using slicing in python
def reverse(A):
    print(A[::-1])
    
A=[1,2,3,4,5,6]
print(A)
print("reversed array/string/list: ")
reverse(A)
