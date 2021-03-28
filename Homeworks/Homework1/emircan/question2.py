user_input = input().split(" ")
mode = int(user_input[0])
number = user_input[1]

# do not change above
# you have both mode and number
# do not forget to print the result
# do your work below
i = 0
string = ""
real_number = int(number)
last_number = 0
remain = ""
binary = []
result = ""

if mode == 0 and real_number == 0:  # escape from 0 0 input
    print(number)

if mode == 0:  # decimal to binary ex. 10 ---> 1010 16*0+8*1+4*0+2*1
    while real_number >= 1:  # divides and keeps the data
        if real_number % 2 == 1:  # checking its value and keeping the data
            remain = "1" + remain
        else:
            remain = "0" + remain
        real_number = real_number // 2  # // stands for receiving integer
    print(remain)

decimal = 0

if mode == 1:  # binary to decimal ex. 0101 ---> 10
    for i in range(len(number)):  # iterates for every digit
        last_number = number[(-i-1)]  # begin with the last number
        decimal = (int(last_number) * 2 ** i) + decimal  # multiply by its decimal value
    print(decimal)
