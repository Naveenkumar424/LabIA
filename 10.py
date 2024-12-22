'''You are developing a library management system that requires a feature to display 
book titles based on their lengths. The goal is to provide librarians with a sorted list of 
book titles to help them identify the shortest and longest titles easily using bubble sort.'''

#title sort
book = list(input("Enter book titles seperated by'-':").split('-'))
print("Unsorted book titles are:",book)
n = len(book)
for i in range(n):
    for j in range(n-i-1):
        if(len(book[j]) > len(book[j+1])):
            book[j],book[j+1] = book[j+1],book[j]
print("Sorted book titles are:",book)
#end of code