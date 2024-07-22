file = "/Users/yatagaclapotk/Desktop/Genel Çalişmalar/adventofcode/2015/day2/input.txt"
with open(file,"r") as f:
#-----------part2--------------------    
    lines = f.readlines()
    ribbonsum = 0
    for line in lines:
        line = line.strip()
        firstocur = line.find("x",0)
        secondocur = line.find("x",firstocur+1)
        length = int(line[0:firstocur])
        width = int(line[firstocur+1:secondocur])
        height = int(line[secondocur+1::])
        ribbonh = length*width*height
        ribbonl = 0
        if length> width:
            if height>= length:
                ribbonl = 2*(length+width)
            else:
                ribbonl = 2*(height+width)
        else:
            if height>width:
                ribbonl = 2*(length+width)
            else:
                ribbonl = 2*(length+height)
        ribbonsum+=ribbonh+ribbonl
    print(ribbonsum)

#-----------part1--------------------

"""     sum = 0
    for line in lines:
        line = line.strip()
        firstocur = line.find("x",0)
        secondocur = line.find("x",firstocur+1)
        length = int(line[0:firstocur])
        width = int(line[firstocur+1:secondocur])
        height = int(line[secondocur+1::])
        sqrfeet = (2*length*width)+(2*width*height)+(2*length*height)
        low = 0
        if length> width:
            if height>= length:
                low = length*width
            else:
                low = height*width
        else:
            if height>width:
                low = length*width
            else:
                low = length*height
        sqrfeet+=low
        sum+=sqrfeet
    print(sum) """