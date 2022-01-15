#while and for loops
#while loops

# x=0
# while (x<5):
#     print(x)
#     x=x+1

#for loops
# for x in range(5,12):
#     print(x)

#arrays
days = ["mon","tue","wed","thur","fri","sat","sun"]
for d in days:
    # if (d=="fri"): break    #loop stops
    if (d=="fri"): continue 
    print(d)
    