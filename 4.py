'''A movie theater needs to organize the prices of its tickets in ascending order 
for display on their website. The theater offers various pricing tiers, and the 
list of prices needs to be sorted so customers can easily view the cheapest options first using selection sort.'''

#def
def sel():
    for i in range(len(a)-1):
        minPos = i
        for j in range(i+1,len(a)):
            if(a[j]<a[minPos]):
                minPos = j
        a[i],a[minPos] = a[minPos],a[i]
#end of def
a = list(input("Enter prices seperated by '-':").split('-'))
print("Unsorted list:",a)
sel()
print("Sorted list:",a)
#end of code