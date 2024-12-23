'''Customer Feedback Sentiment Detection You are developing a customer feedback 
analysis tool for a company. The tool reads through customer feedback and checks for specific 
words associated with either positive or negative sentiments. The goal is to identify if the 
feedback contains a positive or negative sentiment based on a list of predefined keywords, which 
helps the company prioritize responses and assess overall customer satisfaction. .(BFSM)'''

#function
def bfsm(s,ss):
    m = len(s)
    n = len(ss)
    for i in range((m-n)+1):
        if(s[i:(i+n)] == ss):
            return True
    return False
#end of function
#main
feedback = input("Enter a feedback:")
positive = ['good','nice','fast']
negative = ['bad','slow','waste']
p = 0; n = 0
for pos in positive:
    if(bfsm(feedback,pos)):
        p += 1
for neg in negative:
    if(bfsm(feedback,neg)):
        n += 1
if(p > n):
    print("The coustomer has given positive feedback")
else:
    print("The coustomer has given a negative feedback")
#end of code