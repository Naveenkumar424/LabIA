'''Sorting Employee Salaries: You work for a human resources department that needs to analyze employee 
salaries for a report. The report requires sorting the salaries in ascending order to identify the salary 
range and perform further analysis. The system should support sorting a predefined list of salaries or 
allow users to input a new list of salaries dynamically using quick sort.'''

#def 
def quick(a,si,ei):
    if(si > ei):
        return
    pidx = partition(a,si,ei)
    quick(a,si,pidx-1)
    quick(a,pidx+1,ei)
#end of quick
#partition
def partition(a,si,ei):
    pivot = a[ei]
    i = si-1
    for j in range(si,ei):
        if(a[j] < pivot):
            i += 1
            a[i],a[j] = a[j],a[i]
    i += 1
    a[i],a[ei] = pivot,a[i]
    return i
#end of def
#main
ch = int(input("1.Pre-defined\n2.User-defined\nEnter your choice:"))
if(ch == 1):
    a = [2000,6000,3000,10000,7000]
elif(ch == 2):
    a = []
    n = int(input("Enter n:"))
    print(f"Enter {n} elements:")
    for i in range(n):
        a.append(int(input()))
print("Unsorted list:",a)
quick(a,0,len(a)-1)
print("Sorted list:",a)
#end of code