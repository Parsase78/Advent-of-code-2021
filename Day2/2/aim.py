data = open('Day2/2/input.txt', 'r', encoding='utf-8').read().splitlines()
data = [x.split() for x in data]
commands = [(x[0],int(x[1])) for x in data]
h=0 
d=0
a=0 #aim
for cmd,val in commands: 
 if cmd == 'forward': #changing the instructions according to aim 
    h += val
    d += a*val
 elif cmd == 'down':
    a += val
 elif  cmd == 'up':
    a -= val
 else:
    raise ValueError("Invalid input")
print(h*d)