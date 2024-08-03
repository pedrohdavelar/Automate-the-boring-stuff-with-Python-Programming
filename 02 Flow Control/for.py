for i in range(5): 
    print('i is now: ' + str(i)) 

#while equivalent
j = 0
while j < 5:
    print('j is now: ' + str(j))
    j = j + 1  

#different range example
for k in range(10,15):
    print('k is now: ' + str(k))

#different step in range
for l in range(0,11,2):
    print('l is now: ' + str(l)) 

#step can be negative
for m in range(10,-1,-2):
    print('m is now: ' + str(m)) 


#sum of the first 100 integers
total = 0
for num in range(101):
    total = total + num
print(total)