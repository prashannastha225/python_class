#the binary message you want to decode.
binary_input = "01001000 01100101 01101100 01101100 01101111"

#split the string using spaces to get 8 bit blocks
binary_list = binary_input.split()

#convert each block back to a character and join them.
decoded_text = "".join(chr(int(b,2))for b in binary_list)

print(f"decoded: {decoded_text}")