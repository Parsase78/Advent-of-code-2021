

with open('input.txt') as f:
    for lines in f:
        lines = f.readlines()
        numbers = [int(e.strip()) for e in lines]
        count = 1
        for i,j in zip(numbers, numbers[1:]):
                if j > i:
                    count += 1
                    print(count)
                    
                    
        

