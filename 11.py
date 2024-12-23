'''Sorting a List of Product Prices for an E-commerce Platform: 
You are a software developer working on an e-commerce platform that offers various products, 
each with a specific price. The platform aims to enhance user experience by providing a 
seamless browsing experience. As part of this initiative, you need to implement a sorting 
feature that allows customers to view products based on their prices in ascending order using bubble sort.'''

#bubble sort
n = int(input("Enter n:"))
a = []
print(f"Enter {n} elements:")
for i in range(n):
    a.append(int(input()))
print("Unsorted elements:",a)
for j in range(n-1):
    for i in range(n-j-1):
        if(a[i] > a[i+1]):
            a[i],a[i+1] = a[i+1],a[i]
print("Sorted elements:",a)
#end of code