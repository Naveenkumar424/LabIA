'''A company that sells health supplements wants to identify mentions of specific 
keywords within customer reviews to quickly assess customer feedback. 
They want a system that can search for specific keywords (e.g., "excellent," "bad taste," "quick delivery") 
in each review. Given a list of customer reviews, the system should check each review to see if 
it contains any of these keywords and then label the review accordingly.(BFSM)'''

#bfsm
def bfsm(s,ss):
    m = len(s)
    n = len(ss)
    for i in range((m-n)+1):
        if(s[i:(i+n)] == ss):
            return True
    return False
#end of def
#main
reviews = []
n = int(input("Enter n:"))
print(f"Enter {n} elements:")
for i in range(n):
    reviews.append(input())
rc = 0
keywords = ["excellent","bad taste","quick delivery"]
key = input("Enter key:")
if(key in keywords):
    for review in reviews:
        if(bfsm(review,key)):
            rc += 1
    print(f"The keyword {key} has occured {rc}times in {len(reviews)}reviews")
else:
    print("Invalid keyword selected")
#end of code