import hashlib 

inputs = "ckczppom"
#####part1########
inputs1 = "ckczppom117946"
#####part2########
inputs2 = "ckczppom3938038"
number = 0
while True:
    inputplus = inputs + str(number)
    output = hashlib.md5(inputplus.encode())
    out = output.hexdigest()
    #part1
    #if out[0:5] == "00000":
    #part2
    if out[0:6] == "000000":
        print(number)
        break
    else:
        number+=1
out2 = hashlib.md5(inputs2.encode())
print(out2.hexdigest())
