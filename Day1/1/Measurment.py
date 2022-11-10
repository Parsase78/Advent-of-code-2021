with open('Day1/1/input.txt') as f:
    for lines in f:
        lines = f.readlines() # open and read the file per line
        numbers = [int(e.strip()) for e in lines] # store each line as int in a list
        count = 1
        for i,j in zip(numbers, numbers[1:]): # two poiner if statement to compare two indexes
                if j > i:
                    count += 1
                    print(count)
                    
                    
        

