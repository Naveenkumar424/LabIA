'''Write a Python program to find the GCD of two integers using the Middle School Procedure, 
which involves prime factorization and finding common factors.'''

def gcd(m,n):
    md = []
    nd = []
    for i in range(1,m+1):
        if(m%i == 0):
            md.append(i)
    for i in range(1,n+1):
        if(n%i == 0):
            nd.append(i)
    cd = set(md) & set(nd)
    return max(cd)
#end of def
m = int(input("Enter m:"))
n = int(input("Enter n:"))
gcd = gcd(m,n)
print(f"GCD({m},{n})={gcd}")
#end of code