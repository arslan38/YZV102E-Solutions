# taking input
lst = [float(item) for item in input().split()]
# do not change the above

# do your work in below
# fill

lst1 = lst.copy()
lst2 = lst.copy()

length = 0
# length of the list
for i in lst1:
    length += 1
# -----------------------------
min_element = lst[0]
max_element = lst[0]

# min and max
for i in range(length):  #
    if lst1[i] < min_element:
        min_element = lst1[i]

for i in range(length):
    if lst1[i] > max_element:
        max_element = lst1[i]
addition = 0
# -----------------------------
# sum of the list
for i in range(length):
    addition = lst2[i] + addition
# -----------------------------
# indexes of maximum and minimum
index_of_max = length
index_of_min = length
# if a value is smaller/greater and initial, second same value will not be assigned
for i in range(length):
    if lst[i] == min_element and index_of_min > i:
        index_of_min = i
    if lst[i] == max_element and index_of_max > i:
        index_of_max = i
# -----------------------------
mean = addition / length  # calculate mean
variance_addition = 0
for i in range(length):  # sum up all variances between numbers and mean
    variance_addition = (lst[i] - mean) ** 2 + variance_addition

variance = variance_addition / length  # calculating variance by dividing all variances to length

variance = format(variance, '.5f')
min_element = format(min_element, '.5f')
max_element = format(max_element, '.5f')
mean = format(mean, '.5f')
addition = format(addition, '.5f')
# print the desired result
print(length, min_element, index_of_min, max_element, index_of_max, addition, mean, variance)
