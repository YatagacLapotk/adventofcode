filename = "/Users/yatagaclapotk/Desktop/Genel Çalişmalar/adventofcode/2015/day5/input.txt"
with open(filename) as f:
    ###########part1###############
    lines = f.readlines()
    nicenumbers = 0
    for line in lines:
        if line.find("ab")!=-1 or line.find("cd")!=-1 or line.find("pq")!=-1 or line.find("xy")!=-1:
            continue
        else:
            vowelcount = 0
            for i in line:
                if "aeiou".find(i)!=-1:
                    vowelcount+=1
            if vowelcount>=3:
                for j,s in enumerate(line,0):
                    if j < (len(line) - 1) and line[j+1] == s:
                        nicenumbers+=1
                        break
    print(nicenumbers)
    ###########part2###############
    lines = f.readlines()
    nicenumbers = 0
    nicenumbers2 = 0
    for line in lines:
        letterafter = 0
        doubleoverlap = 0
        for i,s in enumerate(line):
            if i <(len(line)-2) and line[i+2] ==s:
                letterafter=1
            if i <(len(line)-1) and line.find(s,i+1)!=-1:
                if line[i+2::].find(line[i:i+2])!=-1:
                    print(line)
                    print(line[i+2::])
                    print(line[i:i+2])
                    doubleoverlap=1
        if letterafter ==1 and doubleoverlap==1:
            nicenumbers+=1 
    print(nicenumbers)
