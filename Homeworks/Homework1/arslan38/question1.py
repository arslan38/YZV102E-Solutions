
# taking input
lst = [float(item) for item in input().split()] 
# do not change the above

# do your work in below
# fill
length=0
minElement= 999999999 # I assigned maximum value for comparison 
minIndex = 0
maxElement = -999999999 # I assigned maximum value for comparison 
maxIndex = 0
sumElements = 0
index = 0
for element in lst:
    length+=1 #calculating len of function
    if element < minElement: #if element is lower than value that I assigned, element become new min value
        minElement = element
        minIndex = index #to get index
    if element > maxElement: #if element is bigger than value that I assigned, element become new max value
        maxElement = element 
        maxIndex = index#to get index
    sumElements+=element #sum of elements
    index+=1 #you said you shouldn't use len function so I use indexin for this value. 
mean = sumElements/length #mean calculation
new_sum = 0 #for variance

for element in lst:
    new_sum += (element - mean)*(element - mean)#sum for variance calculation

variance = new_sum/length#variance calculation
print(f'{length} {minElement:.5f} {minIndex} {maxElement:.5f} {maxIndex} {sumElements:.5f} {mean:.5f} {variance:.5f}')






# print the desired result
