mainList = dict()
rangeNum = range(256) #range of extended ASCII
for i in rangeNum:
    mainList[i] = chr(i)# returns character.

hexDict = {}
listChart = ['a','b','c','d','e','f']
for i in range(10):#first 10 element
    hexDict[str(i)]=i
for j in range(len(listChart)):# for str elements in hexa code
    hexDict[listChart[j]]=j+10#10 to 15

inputHex = input()
sonuc_str = ''
for i in range(len(inputHex)//2):#if there is 10 element we need 0,2,4,6,8 for indexing
    i*=2#1*2 =2 /2*2=4 / 2*3= 6 ...
    variable = inputHex[i]+inputHex[i+1]#for example 456945 is input.I get 45,69 and 45 seperatly with this code
    variableSum = 16*hexDict[variable[0]]+hexDict[variable[1]]#16^1*first+16^0*second
    sonuc_str+=str(mainList[variableSum])

print(mainList)
print(hexDict)
print(sonuc_str)
