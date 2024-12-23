'''Optimal Selection of Equipment for a Camping Trip: You are preparing for a weekend camping trip. 
You have a limited-capacity backpack that can hold a specific weight, and you need to decide which items to pack. 
Each item has a weight and a usefulness value, representing how important it is to have that item during 
your trip.(knapsack).'''

#knapsack
def knap(resources,capacity):
    for resource in resources:
        resource['ratio'] = resource['value']/resource['weight']
    resources.sort(key=lambda x:x['ratio'],reverse = True)
    allocated = []
    totalValue = 0
    for resource in resources:
        if(capacity <= 0):
            break
        weight = resource['weight']
        value = resource['value']
        if(weight <= capacity):
            allocated.append((resource['name'],value,1.0))
            capacity -= weight
            totalValue += value
    return totalValue,allocated
#end of def
#main
n = int(input("Enter n:"))
resources = []
for i in range(n):
    name = input(f"Enter name of item{i+1}:")
    weight = float(input(f"Weight for {name}:"))
    value = float(input(f"Enter value for {name}:"))
    resources.append({'name':name,'weight':weight,'value':value})
capacity = int(input("Enter capacity of knapsack:"))
totalValue,allocated = knap(resources,capacity)
print(totalValue)
print(allocated)
#end of code