'''Data migration using Tower of Hanoi: you are working as a product engineer 
responsible for migration of data from one server to another server due to network and 
bandwidth contents, you can not directly remove large data blocks without first relocating 
smaller data blocks, you also have o access to intermediately server that can be used to store data 
temporally during migration process'''

#function
def tower(n,s,t,d):
    if(n == 1):
        print(f"Move disk {n} from {s} to {d}")
        return
    tower(n-1,s,d,t)
    print(f'Move disk {n} from {s} to {d}')
    tower(n-1,t,s,d)
#end of def
n = int(input("Enter the number of disks:"))
tower(n,'A','B','C')
#end of code