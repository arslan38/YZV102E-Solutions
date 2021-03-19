typeOfCalculation = input()
numberInputs = input()
numberList = []
sonuc = 0
for i in numberInputs.split():
    if i!=' ':numberList.append(int(i))

#######add
if typeOfCalculation.lower()=='a':
    sonuc=numberList[0]+numberList[1]
    print(sonuc)

#######substract
elif typeOfCalculation.lower()=='s':
    sonuc = numberList[0]-numberList[1]
    print(sonuc)

#######multiplication
elif typeOfCalculation.lower()=='m':
    sonuc = numberList[0]*numberList[1]
    print(sonuc)

#######division
elif typeOfCalculation.lower()=='d':
    sonuc = numberList[0]//numberList[1]# // returns integer
    print(sonuc)

#######power
elif typeOfCalculation.lower()=='p':
    sonuc = 1
    for i in range(numberList[1]): #numberList[1] times numberList[0]
        sonuc*=numberList[0]
    print(sonuc)

#######factorial
elif typeOfCalculation.lower()=='f':
    sonuc = 1
    for i in range(1,numberList[0]+1):
        sonuc*=i
    print(sonuc)
         
