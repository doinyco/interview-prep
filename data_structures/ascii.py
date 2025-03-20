# Q: Write a function to convert from ASCII to integer & integer to ASCII.

def char_to_ascii(s):
    return ord(s)

def ascii_to_char(n):
    return chr(n)

s = "C"
ascii = char_to_ascii(s)
print(ascii)
print(hex(ascii))
print(oct(ascii))
print(bin(ascii))
print(ascii_to_char(ascii))

print(ascii_to_char(0x43))
print(ascii_to_char(0b1000011))
print(ascii_to_char(67))