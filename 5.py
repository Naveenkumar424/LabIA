'''A company wants to sort the salaries of its employees from the lowest to the highest for internal analysis. 
Instead of using loops, the company wants to use a recursive approach to sort the list, 
applying a divide-and-conquer technique first using selection sort.'''

#def
def sel(a,i):
    if(i == (len(a))):
        return
    m = minPos(a,i)
    a[i],a[m] = a[m],a[i]
    sel(a,i+1)
#end of sel
#minPos
def minPos(a,i):
    m = i
    for j in range(i+1,len(a)):
        if(a[j]<a[i]):
            m = j
    return m
#end of def
#main
a = []
n = int(input("Enter n:"))
print(f"Enter {n} salaries:")
for i in range(n):
    a.append(int(input()))
print("Unsorted list:",a)
sel(a,0)
print("Sorted list:",a)
#end of code