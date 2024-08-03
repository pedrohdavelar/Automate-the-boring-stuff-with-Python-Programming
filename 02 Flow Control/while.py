print ('How many loops do you want?')
i = int(input())
n = 0
while n < i:
    print('Iteration #' + str(n+1))
    n += 1 

while True:
    print('What is your name?')
    name = input()
    if name == 'Pedro':
        break
print('Yeah, that is your name.')  