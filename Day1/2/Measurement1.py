with open('input.txt') as f:
    for lines in f:
        lines = f.readlines()
        numbers = [int(e.strip()) for e in lines]
        count = 1
        #  depths[i] + depths[i+1] + depths[i+2] < depths[i+1] + depths[i+2] + depths[i+3] ==  depths[i] < depths[i+3]
        for i,j in zip(numbers, numbers[3:]):
                if j > i :
                    count += 1
                    print(count)