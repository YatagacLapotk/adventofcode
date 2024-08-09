import re

filename = "/Users/yatagaclapotk/Desktop/Genel Çalişmalar/adventofcode/2015/day7/input.txt"

with open(filename) as f:
    lines = [x.strip() for x in f.readlines()]
signalist = []

def findlist(l:list,value):
    try:
        l.index(value)
    except:
        return -1

def findsignall(signal:str="a",signalist:list=signalist,lines:list=lines):
    for line in lines:
        s = re.search(f" {signal}$",line)
        if s!=None:
            signalstr = re.findall("[a-z]+",line)
            signalnum = re.findall("[0-9]+",line)
            if findlist(signalist,line)!=-1:
                break
            if signalnum:
                if len(signalstr)>1:
                    findsignall(signalstr[0])
                signalist.append(line)
                break
            findsignall(signalstr[0])
            if len(signalstr)>2:
                findsignall(signalstr[1])
            signalist.append(line)
            
findsignall()

###########part1############
num = {}
for ins in signalist:
    comm = re.findall("[A-Z]+",ins)
    if len(comm) == 0:
        s1,s2 = re.findall("[a-z]+|[0-9]+",ins)
        if s1 == "lx":
            num[s2] = num[s1]
        else:
            num[s2] = int(s1)
    else:
        if comm[0] == "NOT":
            s1,s2 = re.findall("[a-z]+",ins)
            if num.get(s1).is_integer():
                num[s2] = ~ num[s1]
            else:
                num[s2] = ~ int(s1)
        else:
            strings = re.findall("[a-z]+",ins)
            numbers = re.findall("[0-9]+",ins) 
            if len(numbers)!=0:
                s1 = int(numbers[0])
                s2 = int(num[strings[0]])
                s3 = strings[1]
            else:
                s1 = int(num[strings[1]])
                s2 = int(num[strings[0]])
                s3 = strings[2]
            if comm[0]=="AND":
                num[s3] = s1 & s2
            if comm[0]=="OR":
                num[s3] = s1 | s2
            if comm[0]=="LSHIFT":
                num[s3] = s2<<s1
            if comm[0]=="RSHIFT":
                num[s3] = s2>>s1
                     
print(num["a"])
###########part2############
signalist.insert(3,"956 -> b")
num = {}
for ins in signalist:
    comm = re.findall("[A-Z]+",ins)
    if len(comm) == 0:
        s1,s2 = re.findall("[a-z]+|[0-9]+",ins)
        if s1 == "lx":
            num[s2] = num[s1]
        else:
            num[s2] = int(s1)
    else:
        if comm[0] == "NOT":
            s1,s2 = re.findall("[a-z]+",ins)
            if num.get(s1).is_integer():
                num[s2] = ~ num[s1]
            else:
                num[s2] = ~ int(s1)
        else:
            strings = re.findall("[a-z]+",ins)
            numbers = re.findall("[0-9]+",ins) 
            if len(numbers)!=0:
                s1 = int(numbers[0])
                s2 = int(num[strings[0]])
                s3 = strings[1]
            else:
                s1 = int(num[strings[1]])
                s2 = int(num[strings[0]])
                s3 = strings[2]
            if comm[0]=="AND":
                num[s3] = s1 & s2
            if comm[0]=="OR":
                num[s3] = s1 | s2
            if comm[0]=="LSHIFT":
                num[s3] = s2<<s1
            if comm[0]=="RSHIFT":
                num[s3] = s2>>s1
                     
print(num["a"])
            





            
            