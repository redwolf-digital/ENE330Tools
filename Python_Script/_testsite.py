
import telnetlib 
import numpy as np


print("Test site run")

testData = "ST,52,45,44,57,4F,4C,46,20,44,69,47,69,54,41,4C,SP"


tn = telnetlib.Telnet("192.168.1.52", 7)

tn.open('192.168.1.52', 7 , 1000)

# tn.write(b"" + bytes.fromhex("67"))
tn.write(b"g")

# Print the output 
dataIn = tn.read_until(b"SP").decode('utf-8')
dataArr = np.char.split(dataIn, sep=",")
datalist = dataArr.tolist()

print(dataIn)

if datalist[len(datalist)-1] == 'SP' :
    dataHex = [int(x, 16) for x in datalist[1:len(datalist)-1]]
    print(dataHex)
else :
    print("ERROR") 



if dataIn == testData :
    print("PASS")
else :
    print("ERROR")