user_input = input().split(" ")
mode = int(user_input[0])
number = user_input[1]



# do not change above
# you have both mode and number
# do not forget to print the result
# do your work below

bolumlerList=[]
x = number

if mode==0:
    x = int(x) #we need int x value because we will do some calculations
    flag = True#necessary for loop
    while flag:
        if x<2: # I just divide 2 while number cannot be dividible to 2
            toplam = ''
            for i in bolumlerList[::-1]:toplam+=str(i)#I did string sum for getting all values side by side from reverse way.
            sonuc = str(x)+toplam # last residual is x. I did a string sum for same reason with above.
            print(sonuc)
            flag = False #for finishing loop 
        else:
            bolumlerList.append(x%2)# I just add all divisions to list for sum
            x = int(x/2)
elif mode==1:
    sumforConvert = 0 
    index=len(x)-1 #For exponent calculation 
    for digit in x: # all elements on string x // '1010' -> '1','0','1','0'
        sumforConvert+=int(digit)*(2**index) # 1010 -> 1*2^3+0*2^2+1*2^1+0*2^0
        index-=1 # for exponent calculation 
    print(sumforConvert)



    
	
