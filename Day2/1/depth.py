data = open('Day2/1/input.txt', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data] # Read and Split the data into a list
commands = [(x[0],int(x[1])) for x in data] # iteerate through string and integer separately
h=0 #horizontal
d=0 #depth
for cmd,val in commands: #define the logic of puzzle
 if cmd == 'forward':
    h += val
 elif cmd == 'down':
    d += val
 elif  cmd == 'up':
    d -= val
 else:
    raise ValueError("Invalid input")
print(h*d) #final answer


    

