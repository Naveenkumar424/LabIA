'''You work in a real estate company and need to analyze property prices across different regions. 
You have a list of property prices and need to determine the highest and lowest prices using a 
divide-and-conquer approach with array splitting. This will help in understanding price ranges 
across different regions and make better investment decisions.(find MIN and MAX)'''

#function
def minMax(a,low,high):
    if(low == high):
        return a[low],a[high]
    mid = (low+high)//2
    lmi,lma = minMax(a,low,mid)
    rmi,rma = minMax(a,mid+1,high)
    min = lmi; max = lma
    if(lmi > rmi):
        min = rmi
    if(lma < rma):
        max = rma
    return min,max
#ens of def
#main
a = []
n = int(input("Enter n:"))
print(f"Enter {n} property prices:")
for i in range(n):
    a.append(int(input()))
min,max = minMax(a,0,len(a)-1)
print(f"Minimum property price is {min} and Maximum property price is {max}")
#end of code