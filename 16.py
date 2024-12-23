'''A company managing electric vehicle (EV) charging stations wants to send a technician to perform 
maintenance on multiple stations in a region. Each station is connected to others by a road network, 
and the distances between stations are known. The technician must visit each station once, starting and 
ending at the main station. The company wants to optimize the route to minimize travel distance. .(TSP)'''

#tsp using graph
def createGraph():
    n = int(input("Enter n:"))
    station = []
    graph = {}
    for i in range(n):
        name = input(f"Enter name of station{i+1}:")
        graph[name]={}
        station.append(name)
    for i in range(n):
        for j in range(i+1,n):
            dis = int(input(f"Enter distnce between station{station[i]} and {station[j]}"))
            graph[station[i]][station[j]] = dis
            graph[station[j]][station[i]] = dis
    return station,graph
#end of graph
#genPerm
def genPerm(station):
    if(len(station) == 1):
        return [station]
    per = []
    for i in range(len(station)):
        curr = station[i]
        rem = station[:i]+station[i+1:]
        for perm in genPerm(rem):
            per.append([curr]+perm)
    return per
#end of perm
#cal 
def cal(route,graph):
    total = 0
    for i in range(len(route)-1):
        total += graph[route[i]][route[i+1]]
    total += graph[route[-1]][route[0]]
    return total
#end of cal
#tsp
def tsp(station,graph):
    minDis = float('inf')
    shortestRoute = None
    for route in genPerm(station):
        currDis = cal(route,graph)
        if(currDis < minDis):
            minDis = currDis
            shortestRoute = route
    return minDis,shortestRoute
#end of tsp
#main
station,graph = createGraph()
minDis,shortestRoute = tsp(station,graph)
print("Minimum distance:",minDis,"\nShortest route:",shortestRoute)
#end of code