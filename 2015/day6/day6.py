import re

filename = "/Users/yatagaclapotk/Desktop/Genel Çalişmalar/adventofcode/2015/day6/input.txt"

with open(filename) as f:
    lines = [x.strip() for x in f.readlines()]
###########part1###############
lights = [[0]*1000 for row in range(1000)]
for line in lines:
    number1x1,number1x2,number2x1,number2x2 = [int(x) for x in re.findall(r'\d+',line)] 
    number2x1+=1
    number2x2+=1
    ins = re.search("(turn on|turn off|toggle)",line).group()
    for x in range(number1x1,number2x1):
        for y in range(number1x2,number2x2):
            if ins == "turn on":
                    lights[x][y] = 1
            elif ins == "turn off":
                lights[x][y] = 0
            elif ins == "toggle":
                lights[x][y] = 1- lights[x][y]

sum1 = sum(sum(row) for row in lights)
print(sum1)
###########part2###############
lights2 = [[0]*1000 for row in range(1000)]
for line in lines:
    number1x1,number1x2,number2x1,number2x2 = [int(x) for x in re.findall(r'\d+',line)] 
    number2x1+=1
    number2x2+=1
    ins = re.search("(turn on|turn off|toggle)",line).group()
    for x in range(number1x1,number2x1):
        for y in range(number1x2,number2x2):
            if ins == "turn on":
                    lights2[x][y] += 1
            elif ins == "turn off":
                if lights2[x][y]>0:
                    lights2[x][y] -= 1
            elif ins == "toggle":
                lights2[x][y] +=2

sum2 = sum(sum(row) for row in lights2)
print(sum2)

                            


  


