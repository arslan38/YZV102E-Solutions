# Table of Contents
- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)

 ----

## Question 1


#### You will be given a list, assume the list will not be empty, consists of floats. You are required to compute some statistical values according to given definitions and formulas.

- Length: Number of elements in the list: N

- Minimum: Minimum element of the list and its index number.

- Max: Maximum element of the list and its index number.

- Sum: Summation of the list.

- Mean: Mean of the list: 

- Variance: Mean of the list: 
 
### Note:

- Do not forget to count from 0 for index number.

- In the case of multiple maximum/maximum number, smallest index will be accepted.

- Do not use any built-in function like len, mean, etc. otherwise, you will not get any points! The aim is to calculate necessary values by iterating over the list.
 
### Input Format

- Space seperated float values 3.14 2 53 12.2

### Constraints

- -999999999 <= x >= 999999999
- 0 < N <= 50

### Output Format
Space Seperated Statistical Values with Precision 5

- {Length} {Minimum with precision 5} {Minimum Index} {Maximum with precision 5} {Maximum Index} {Sum with precision 5} {Mean with precision 5} {Variance with precision 5}

- 4 2.00000 1 53.00000 2 70.34000 17.58500 433.69268

Sample Input 0
```
3.14 2 53 12.2
```
Sample Output 0
```
4 2.00000 1 53.00000 2 70.34000 17.58500 433.69268
```
----



## Question 2

#### Binary numbers are used in computer and communications systems. So the conversion is important. In this problem we will focus to this conversions.

### Note: 

- You are not allowed to use built-in functions for conversions!

### Input Format

- mode number

- 0 10

- 1 1010

- mode = 0 ->  Decimal to Binary Conversion

- mode = 1 ->  Binary to Decimal Conversion

### Constraints

- mode ∈ [0,1] 

- number >= 0

### Output Format

- Result

Sample Input 0
```
0 10
```
Sample Output 0
```
1010
```
----


## Question 3


#### In this part you are required follow a procedure that shown below;

- Create a Look-up Table for Ascii Characters Ascii code is a way to store data in the computers. Every hexadecimal number corresponds to a character. You can check the table in here. You are required create a look-up table with dictionary type. Keys are integer values between 0 and 255. Values are the characters in the ascii table. Finally print the dictionary.
- Create a Look-up Table for Hexadecimal to Decimal In hexadecimal numbers there are 16 numbers which are {1,2,3,4,5,6,7,8,9,a,b,c,d,e,f} . You need to create dictionary whose keys are hexadecimal number as string format, and the values are the decimal correspondings. Finally print the dictionary.

- Conversion It is the final step. First take an input from the user. Then convert every 2 hexadecimal numbers to Ascii character by using the dictionaries made up above. Then print the converted string. For example: Input = "464748494A" Output = "FGHIJ"
 
### Note:

- You are not allowed to use built-in functions for conversions!

### Input Format

- String in hexadecimal format. Characters will be lower case so the numbers are 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f

### Constraints

- Input in Hexadecimal format and the length of the input is multiple of two

### Output Format
- Printed dictionary whose keys are 0 to 255 where keys are sorted ascending you need to be careful! printed dictionary whose keys are 0 to f where keys are sorted ascending you need to be careful! converted text.

Sample Input 0
```
4954552031373733
```
Sample Output 0
```
{0: '\x00', 1: '\x01', 2: '\x02', 3: '\x03', 4: '\x04', 5: '\x05', 6: '\x06', 7: '\x07', 8: '\x08', 9: '\t', 10: '\n', 11: '\x0b', 12: '\x0c', 13: '\r', 14: '\x0e', 15: '\x0f', 16: '\x10', 17: '\x11', 18: '\x12', 19: '\x13', 20: '\x14', 21: '\x15', 22: '\x16', 23: '\x17', 24: '\x18', 25: '\x19', 26: '\x1a', 27: '\x1b', 28: '\x1c', 29: '\x1d', 30: '\x1e', 31: '\x1f', 32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 127: '\x7f', 128: '\x80', 129: '\x81', 130: '\x82', 131: '\x83', 132: '\x84', 133: '\x85', 134: '\x86', 135: '\x87', 136: '\x88', 137: '\x89', 138: '\x8a', 139: '\x8b', 140: '\x8c', 141: '\x8d', 142: '\x8e', 143: '\x8f', 144: '\x90', 145: '\x91', 146: '\x92', 147: '\x93', 148: '\x94', 149: '\x95', 150: '\x96', 151: '\x97', 152: '\x98', 153: '\x99', 154: '\x9a', 155: '\x9b', 156: '\x9c', 157: '\x9d', 158: '\x9e', 159: '\x9f', 160: '\xa0', 161: '��', 162: '��', 163: '��', 164: '��', 165: '��', 166: '��', 167: '��', 168: '��', 169: '��', 170: '��', 171: '��', 172: '��', 173: '\xad', 174: '��', 175: '��', 176: '��', 177: '��', 178: '��', 179: '��', 180: '��', 181: '��', 182: '��', 183: '��', 184: '��', 185: '��', 186: '��', 187: '��', 188: '��', 189: '��', 190: '��', 191: '��', 192: '��', 193: '��', 194: '��', 195: '��', 196: '��', 197: '��', 198: '��', 199: '��', 200: '��', 201: '��', 202: '��', 203: '��', 204: '��', 205: '��', 206: '��', 207: '��', 208: '��', 209: '��', 210: '��', 211: '��', 212: '��', 213: '��', 214: '��', 215: '��', 216: '��', 217: '��', 218: '��', 219: '��', 220: '��', 221: '��', 222: '��', 223: '��', 224: '��', 225: '��', 226: '��', 227: '��', 228: '��', 229: '��', 230: '��', 231: '��', 232: '��', 233: '��', 234: '��', 235: '��', 236: '��', 237: '��', 238: '��', 239: '��', 240: '��', 241: '��', 242: '��', 243: '��', 244: '��', 245: '��', 246: '��', 247: '��', 248: '��', 249: '��', 250: '��', 251: '��', 252: '��', 253: '��', 254: '��', 255: '��'}
{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
ITU 1773
```
----


