'''Write a Python program to calculate the GCD of two integers 
by checking all integers from 1 up to the smaller of the two numbers.'''

#consecutive integer checking
def gcd(m,n,t):
    if(m%t ==0 and n%t == 0):
        return t
    return gcd(m,n,t-1)
#end of def
#main
m = int(input("Enter m:"))
n = int(input("Enter n:"))
gcd = gcd(m,n,min(m,n))
print(f"GCD({m},{n})={gcd}")
#end of code