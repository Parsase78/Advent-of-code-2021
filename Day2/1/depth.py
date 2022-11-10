data = open('Day2/1/input.txt', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data]
commands = [(x[0],int(x[1])) for x in data]
h=0 
d=0
for cmd,val in commands: 
 if cmd == 'forward':
    h += val
 elif cmd == 'down':
    d += val
 elif  cmd == 'up':
    d -= val
 else:
    raise ValueError("Invalid input")
print(h*d)


    

