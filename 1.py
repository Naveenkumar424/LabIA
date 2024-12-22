'''Write a Python program to compute the GCD of two integers using the Euclidean Algorithm.'''

#def
def gcd(m,n):
    if(n == 0):
        return m
    if(m < n):
        return gcd(n,m)
    return gcd(n,m%n)
#end of def
#main
m = int(input("Enter m:"))
n = int(input("Enter n:"))
gcd = gcd(m,n)
print(f"GCD({m},{n})={gcd}")
#end of code