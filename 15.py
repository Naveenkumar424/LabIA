'''A courier company wants to optimize the delivery route for a driver who has to deliver 
packages to multiple destinations. The driver starts from a central hub, visits all destinations, 
and then returns to the hub. The company needs to find the shortest possible route, considering 
the distances between each pair of destinations.(TSP)'''

#tsp
def genPerm(cities):
    if(len(cities) == 1):
        return [cities]
    per = []
    for i in range(len(cities)):
        curr = cities[i]
        rem = cities[:i]+cities[i+1:]
        for perm in genPerm(rem):
            per.append([curr]+perm)
    return per
#end of genperm
#cal
def cal(route,distance):
    total = 0
    for i in range(len(route)-1):
        total += distance[route[i]][route[i+1]]
    total += distance[route[-1]][route[0]]
    return total
#end of cal
#tsp
def tsp(distance):
    cities = list(range(len(distance)))
    shortestRoute = None
    minDis = float('inf')
    for route in genPerm(cities):
        currDis = cal(route,distance)
        if(currDis < minDis):
            minDis = currDis
            shortestRoute = route
    return minDis,shortestRoute
#end of tsp
distance = [[0,10,15,20],
            [10,0,35,25],
            [15,35,0,30],
            [20,25,30,0]]
minDis,shortestRoute = tsp(distance)
print("Minimum distance:",minDis,"\nShortest route:",shortestRoute)
#end of code