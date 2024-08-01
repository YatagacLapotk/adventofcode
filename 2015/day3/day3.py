filename = "/Users/yatagaclapotk/Desktop/Genel Çalişmalar/adventofcode/2015/day3/input.txt"
with open(filename , "r") as f:
    
###########PART1#################
    left = "<"
    right = ">"
    up = "^"
    down = "v"
    housesum = 1 
    height = 0
    width = 0 
    houses = {1:[0,0]}  
    line = f.readline()
    for s in line:
        if s is left:
            width-=1
        elif s is right:
            width+=1
        elif s is down:
            height-=1
        elif s is up:
            height+=1
        equal = 0
        for v in houses.values():
            if [width,height] == v:
                equal = 1
                break
        if equal != 1:
            housesum+=1
            houses[housesum] = [width,height]
    print(housesum)
###########PART2################# 
    left = "<"
    right = ">"
    up = "^"
    down = "v"
    housesum = 1 
    height1 = 0
    width1 = 0 
    height2 = 0
    width2 = 0
    houses = {1:[0,0]}  
    line = f.readline()
    for i,s in enumerate(line):
        equal = 0
        if i%2==1:
            if s is left:
                width2-=1
            elif s is right:
                width2+=1
            elif s is down:
                height2-=1
            elif s is up:
                height2+=1
            for v in houses.values():
                if [width2,height2] == v:
                    equal = 1
                    break
            if equal != 1:
                housesum+=1
                houses[housesum] = [width2,height2]  
        else:
            if s is left:
                width1-=1
            elif s is right:
                width1+=1
            elif s is down:
                height1-=1
            elif s is up:
                height1+=1 
            for v in houses.values():
                if [width1,height1] == v:
                    equal = 1
                    break
            if equal != 1:
                housesum+=1
                houses[housesum] = [width1,height1]
    print(housesum) 
    
