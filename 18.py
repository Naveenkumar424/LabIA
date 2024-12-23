'''Resource Allocation for a Conference: A conference organizer needs to allocate various resources 
(e.g., refreshments, materials, and decorations) to a limited budget. Each type of resource has a specific
cost and value (profit), and the total budget limits the amount that can be spent on each resource. 
Resources can be allocated in fractional amounts if needed.
( Fractional Knapsack Problem: Resource Allocation).'''

#def
def frac(resources,budget):
    for resource in resources:
        resource['ratio'] = resource['value']/resource['cost']
    resources.sort(key=lambda x:x['ratio'],reverse=True)
    allocated = []
    totalValue = 0
    for resource in resources:
        if(budget <= 0):
            break
        cost = resource['cost']
        value = resource['value']
        if(cost <= budget):
            allocated.append((resource['name'],value,1.0))
            totalValue += value
            budget -= cost
        else:
            fr = value/cost
            allocated.append((resource['name'],value,fr))
            totalValue += int(fr)
            budget = 0
    return totalValue,allocated
#end of def
#main
n = int(input("Enter n:"))
resources = []
for i in range(n):
    name = input(f"Enter name of item{i+1}:")
    weight = float(input(f"Weight for {name}:"))
    value = float(input(f"Enter value for {name}:"))
    resources.append({'name':name,'cost':weight,'value':value})
capacity = int(input("Enter capacity of knapsack:"))
totalValue,allocated = frac(resources,capacity)
print(totalValue)
print(allocated)
#end of code