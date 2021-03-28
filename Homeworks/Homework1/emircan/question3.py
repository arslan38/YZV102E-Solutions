ascii_table = {}

hexadecimal_table = {}  # dictionary

hexadecimal_lst = ["a", "b", "c", "d", "e", "f"]

for i in range(256):  # for each 255 character
    ascii_table[i] = (chr(i))  # filling ascii dictionary

for i in range(16):  # filling hexadecimal dictionary
    if 0 <= i < 10:  # separate processes
        hexadecimal_table[str(i)] = i
    if i > 9:
        hexadecimal_table[hexadecimal_lst[i-10]] = i

string = input().lower()  # considering about lower, upper case
lst = [string[i:i+2] for i in range(0, len(string), 2)]
"""
putting input into a list two by two, range is 0 to length of the string
"""
dual = ""
will = ""  # wanted output
call = 0
b = 0
c = 0
d = 0

for i in range(len(lst)):  # coming from list to digit
    dual = lst[i]  # dual = 4A
    for digit in range(2):  # iterates for every digit
        call = hexadecimal_table.get(dual[digit])  # 4 a keys --> 4 10 values
        if digit % 2 == 0:  # sixteens digit
            b = call * 16
        else:  # units digit
            c = call
    d = b + c
    will = will + ascii_table[d]

print(ascii_table)
print(hexadecimal_table)
print(will)
