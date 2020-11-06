"""
Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

Every eight bits in the binary string represents one character on the ASCII table.

Examples:

csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
01101100 -> 108 -> "l"
01100001 -> 97 -> "a"
01101101 -> 109 -> "m"
01100010 -> 98 -> "b"
01100100 -> 100 -> "d"
01100001 -> 97 -> "a"
csBinaryToASCII("") -> ""
------------------------------------------------------
Notes:

The input string will always be a valid binary string.
Characters can be in the range from "00000000" to "11111111" (inclusive).
In the case of an empty input string, your function should return an empty string.
[execution time limit] 4 seconds (py3)
-------------------------------------------------------
My notes 
65 is an uppercase 'A', and 97 is a lowercase 'a'.
For each set of 8 binary digits, convert it to a number, 
and look it up in an ASCII table.
01000100 as 2^6+2^2=68 directly.

-----------------------------------------------------------
[input] string binary

[output] string

[Python 3] Syntax Tips
"""



def csBinaryToASCII(binary):
    return ''.join(chr(int(binary[i*8:i*8+8], 2)) for i in range(len(binary)//8))
     


print(csBinaryToASCII("011011000110000101101101011000100110010001100001")) # -> "lambda"
print(csBinaryToASCII("")) # -> ""


 
